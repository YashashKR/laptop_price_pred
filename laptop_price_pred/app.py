from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model/laptop_price_model.h5')

# Pre-determined columns based on the training data after one-hot encoding
expected_columns = [
    'brand_...', 'processor_brand_...', 'processor_name_...',  # Replace with actual one-hot encoded columns
    'ram_gb', 'ram_type_...', 'ssd', 'hdd', 'os_...', 'os_bit'
    # Continue with all the one-hot encoded features from the original training data
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve form data
            brand = request.form['brand']
            processor_brand = request.form['processor_brand']
            processor_name = request.form['processor_name']
            ram_gb = float(request.form['ram_gb'])
            ram_type = request.form['ram_type']
            ssd = float(request.form['ssd'])
            hdd = float(request.form['hdd'])
            os = request.form['os']
            os_bit = float(request.form['os_bit'])

            # Prepare input for the model
            input_features = pd.DataFrame([{
                'brand': brand,
                'processor_brand': processor_brand,
                'processor_name': processor_name,
                'ram_gb': ram_gb,
                'ram_type': ram_type,
                'ssd': ssd,
                'hdd': hdd,
                'os': os,
                'os_bit': os_bit
            }])

            # One-hot encode categorical variables
            input_features = pd.get_dummies(input_features)

            # Ensure all expected columns are present
            for col in expected_columns:
                if col not in input_features.columns:
                    input_features[col] = 0

            # Reorder columns to match the model's input shape
            input_features = input_features.reindex(columns=expected_columns, fill_value=0)

            # Predict the price
            prediction = model.predict(input_features)[0][0]

            return render_template('index.html', prediction=f'Predicted Laptop Price: ${prediction:.2f}')
        except Exception as e:
            return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
