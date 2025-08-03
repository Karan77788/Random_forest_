from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model, features = joblib.load('breast_cancer_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        input_data = []
        for feature in features:
            val = float(request.form[feature])
            input_data.append(val)

        df = pd.DataFrame([input_data], columns=features)
        result = model.predict(df)[0]
        prediction = "Malignant" if result == 1 else "Benign"

    return render_template('result.html', features=features, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
