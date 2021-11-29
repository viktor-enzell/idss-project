import pickle
import pandas as pd
import numpy as np
from django.conf import settings


class RentPredictor:
    def __init__(self):
        model_dir = f'{settings.BASE_DIR}/models/'
        self.model = pickle.load(open(f'{model_dir}rent_model.sav', 'rb'))
        self.one_hot_encoder = pickle.load(open(f'{model_dir}rent_encoder.sav', 'rb'))
        self.all_features = ['room_type', 'district', 'accommodates', 'bedrooms']
        self.categorical_features = ['room_type', 'district']

    def predict(self, room_type, district, accommodates, bedrooms):
        all_inputs = pd.DataFrame(
            data=np.array([[room_type, district, accommodates, bedrooms]]),
            columns=self.all_features
        )
        one_hot_categorical_inputs = pd.DataFrame(
            data=self.one_hot_encoder.transform(all_inputs[self.categorical_features]),
            columns=self.one_hot_encoder.get_feature_names_out(input_features=self.categorical_features)
        )
        preprocessed_inputs = pd.concat(
            [all_inputs, one_hot_categorical_inputs], axis=1
        ).drop(columns=self.categorical_features, axis=1)

        return int(self.model.predict(preprocessed_inputs)[0])
