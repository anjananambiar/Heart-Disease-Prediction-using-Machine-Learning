import numpy as np
import pickle

# Load the trained model from the 'model.pkl' file
with open('model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Function to get user input for features
def get_user_input():
    age = float(input("Enter age: "))
    sex = float(input("Enter gender (1 for male, 0 for female): "))
    cp = float(input("Enter chest pain type (between 1 to 3): "))
    trestbps = float(input("Enter resting blood pressure (average around 120/80 mm Hg): "))
    chol = float(input("Enter serum cholesterol (average around 200 mg/dL): "))
    
    # Modify the input prompt for fasting blood sugar to avoid escape sequences
    fbs = float(input("Enter fasting blood sugar (1 for true, 0 for false): "))
    
    restecg = float(input("Enter resting electrocardiographic results (0 or 1): "))
    thalach = float(input("Enter maximum heart rate achieved (average around 150): "))
    exang = float(input("Enter exercise-induced angina (1 for yes, 0 for no): "))
    oldpeak = float(input("Enter ST depression induced by exercise relative to rest (between 0-6 including decimal but average containing between 0-1): "))
    slope = float(input("Enter slope of the peak exercise ST segment (0-2): "))
    ca = float(input("Enter number of major vessels (0-3) colored by fluoroscopy: "))
    thal = float(input("Enter thallium stress test result (0-3): "))
    
    return np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)

# Get user input
user_input = get_user_input()

# Make prediction using the loaded model
probability_of_heart_disease = loaded_model.predict(user_input)

# Convert probability to percentage
percentage_probability = probability_of_heart_disease[0] * 100

# Check if the probability is equal to or greater than 1
if probability_of_heart_disease[0] >= 1:
    print("You have heart disease.")
else:
    print(f"Predicted probability of heart disease: {percentage_probability:.2f}%")
