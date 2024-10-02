# Well Water Prediction

This is a Streamlit-based application that predicts well water levels using data from the Central Ground Water Board (CGWB). The application utilizes machine learning models, with the Random Forest Regressor being the best-performing model for prediction. Other models such as LSTM and Linear Regressor were tested but did not achieve the same level of accuracy as the Random Forest model. The application is designed for local use and has not been deployed yet.

## Features

The Well Water Prediction Application provides the following features:

1. **Water Level Prediction**: Users can predict the future water levels of wells by inputting data about location, rainfall and discharge. The Random Forest Regressor model analyzes the data to provide accurate predictions of water levels.

2. **Model Accuracy Graphs**: Users can check the predicted values and actual values of the testing data plotted on graph and verify the model accuracy.

## Installation

To run the Well Water Prediction Application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Ace-9136/well-water-prediction
    ```

2. Change to the project directory:
    ```bash
    cd well-water-prediction
    ```

3. Set up a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Install Streamlit if it's not already installed:
    ```bash
    pip install streamlit
    ```

6. Start the Streamlit application:
    ```bash
    streamlit run app.py
    ```

7. Open your browser and navigate to http://localhost:8501 to access the application.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request.

## License

This project is licensed under the MIT License.
