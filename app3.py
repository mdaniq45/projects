
import streamlit as st
import numpy as np

# Load the saved StandardScaler (sc) and LogisticRegression model (classifier)
# Assuming that 'sc' and 'classifier' have been trained and saved before

# Example: If you have these saved, load them using joblib/pickle
import joblib
sc = joblib.load('scaler.pkl')
classifier = joblib.load('logistic_model.pkl')

# Streamlit App
st.title('Product Purchase Prediction')

# Input features from user
age = st.number_input('Enter Age:', min_value=18, max_value=100, value=30)
salary = st.number_input('Enter Salary:', min_value=0, max_value=100000, value=50000)

# Button to make predictions
if st.button('Predict'):
    # Feature scaling
    user_input = np.array([[age, salary]])
    user_input_scaled = sc.transform(user_input)  # Scale the input using the StandardScaler
    
    # Predict using the classifier
    prediction = classifier.predict(user_input_scaled)
    
    # Display the result
    if prediction == 1:
        st.success('The person is likely to purchase the product.')
    else:
        st.error('The person is unlikely to purchase the product.')

