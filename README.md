# Intelligent Decision Support System
An application for analyzing the profitability of apartment investments in Barcelona. The app is built as a Django website where a user inputs information about a potential apartment investment. The app then analyzes the data and uses machine learning models to give insight into the potential profitability of the investment.


## Project structure
The project follows the standard structure of a Django project with a few additions.
```
models/                 <-- Price-prediction and rent-prediction models and data
project/                <-- Django app containing source code
  templates/            <-- User interface
  views.py              <-- Django views, providing the connection between the app and the interface
  price_predictor.py    <-- Python class for interacting with the price-prediction model
  rent_predictor.py     <-- Python class for interacting with the rent-prediction model
  profit_predictor.py   <-- Python class for generating profit insights
  wacc_predictor.py     <-- Calculating Weighted Average Capital Cost
  openai_api.py         <-- Python class for interacting with GPT-3
  ...
static/
...
```

[This AirBnb dataset](https://www.kaggle.com/fermatsavant/airbnb-dataset-of-barcelona-city?select=barca.csv) is used for creating a rent-prediction model, and [this Idealista dataset](https://www.kaggle.com/jorgeglez/barcelona-idealista-housingprices) is used for creating a price-prediction model.


## Running the application
Start by installing the required packages for the project. It is recommended to start a new virtual environment in Python before installing the requirements. 
```
pip install -r requirements.txt
```
Start the Django server with the following command.
```
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/ in your browser to interact with the app.

#### Optional
An experimental feature where the language model GPT-3 is used to generate a description of the apartment can be enabled by following these instructions.
1. Navigate to the [OpenAI API](https://beta.openai.com/overview) and create an account.
2. Retrieve an API key from the OpenAI website.
3. Create a file named `.env` in the root of the Django project and add the following line `OPENAI_API_KEY=key`, replacing `key` with your OpenAI API key.

