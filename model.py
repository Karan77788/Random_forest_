import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("breast_cancer_sample.csv")

features = ['RadiusMean', 'TextureMean', 'PerimeterMean', 'AreaMean', 'SmoothnessMean']
X = df[features]
y = df['Diagnosis'].map({'M': 1, 'B': 0})  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump((model, features), 'breast_cancer_model.pkl')
print(" Model trained and saved.")
