import pickle
import pandas as pd
import numpy as np
from django.conf import settings


class PricePredictor:
    def __init__(self):
        model_dir = f'{settings.BASE_DIR}/models/'
        self.model = pickle.load(open(f'{model_dir}house_price_model.sav', 'rb'))
        self.one_hot_encoder = pickle.load(open(f'{model_dir}house_price_encoder.sav', 'rb'))
        self.all_features = ['district', 'neighborhood', 'condition', 'type', 'rooms', 'area_m2', 'lift', 'views', 'floor']
        self.categorical_features = ['district', 'neighborhood', 'condition', 'type', 'lift', 'views', 'floor']

    def predict(self, district, neighborhood, condition, apt_type, rooms, area_m2, lift, views, floor):
        all_inputs = pd.DataFrame(
            data=np.array([[district, neighborhood, condition, apt_type, rooms, area_m2, lift, views, floor]]),
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
