# Random_forest_
# Breast Cancer Diagnosis Predictor
A simple web application built using Flask and Random Forest Classifier to predict whether a breast tumor is Malignant or Benign based on selected features from the Breast Cancer Wisconsin dataset.

# Project Structure
```
├── app.py                   # Flask backend
├── model.py                 # Model training script
├── breast_cancer_model.pkl  # Trained model and features (saved with joblib)
├── breast_cancer_sample.csv # Dataset used for training
├── templates/
│   └── result.html          # Frontend HTML
├── static/
│   └── style.css            # CSS for styling
└── requirements.txt         # Python dependencies
```
# Features Used
```
Radius Mean
Texture Mean
Perimeter Mean
Area Mean
Smoothness Mean
```
These features are selected to keep the UI simple while maintaining model accuracy.

# Getting Started

1. Clone the Repository
```
git clone https://github.com/your-username/breast-cancer-predictor.git
cd breast-cancer-predictor
```
2. Install Dependencies
Make sure Python is installed (preferably 3.9+), then run:
```
pip install -r requirements.txt
```
3. Train the Model (if not already done)
```
python model.py
```
This will save breast_cancer_model.pkl in the root directory.

4. Run the Flask App
```
python app.py
```
Visit: http://127.0.0.1:5000/ in your browser.

# UI Overview
A simple form with fields for each of the 5 input features.

Submit the form to see if the tumor is Malignant or Benign.

Clean and responsive UI styled with style.css.

#  Model Details
```
Algorithm: RandomForestClassifier

Training/Test Split: 80/20

Dataset: breast_cancer_sample.csv

Label Mapping: M → 1, B → 0
```
# Requirement
```
Flask
scikit-learn
pandas
joblib
```
# ScreenShots
![alt text](<Screenshot 2025-08-03 114150.png>)
![alt text](<Screenshot 2025-08-03 114522.png>)
![alt text](<Screenshot 2025-08-03 114503.png>)

