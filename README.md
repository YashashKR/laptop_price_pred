# Laptop Price Prediction

This project is a for predicting laptop prices based on various specifications. The model is trained using TensorFlow and deployed using Flask. Users can input laptop specifications, and the app predicts the price using the trained machine learning model.

## Project Structure

```
laptop_price_pred/
│
├── app.py              # Flask application
├── model/
│   └── laptop_price_model.h5  # Trained TensorFlow model
├── templates/
│   └── index.html      # HTML file for the web interface
├── static/
│   └── style.css       # CSS file for styling (optional)
└── requirements.txt    # Python dependencies

```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/laptop-price-prediction.git
   cd laptop-price-prediction
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the trained model in the `model/` directory.

## Running the App

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the app.

## Screenshot

![Image](https://github.com/user-attachments/assets/25c07ecd-5c74-452b-ae12-a1a35bb681e2)

## How to Use

1. Enter the laptop specifications in the provided form.
2. Click the "Predict" button.
3. View the predicted laptop price on the result page.

## Model Training

To retrain the model, follow these steps:

1. Load the dataset (ensure it has appropriate columns for specifications and target price).
2. Preprocess the data by handling categorical features using one-hot encoding.
3. Split the data into training, validation, and test sets (70%, 15%, 15%).
4. Train the model using TensorFlow.
5. Save the trained model in the `model/` directory.

Refer to the `app.py` file for more details on input handling and prediction logic.

## Dependencies

- Flask
- TensorFlow
- Pandas
- NumPy

## dependencies using the requirements
Flask,
tensorflow,
numpy,
pandas.


