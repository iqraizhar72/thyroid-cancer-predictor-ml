from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def makeprediction():
    with open('logmodel.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

@app.route('/getprediction', methods=['POST'])
def getpredict():
    # Mapping for categorical inputs
    gender_map = {'male': 1.0, 'female': 0.0}
    yesno_map = {'no': 0.0, 'yes': 1.0}
    rlevel_map = {'low': 1.0, 'medium': 2.0, 'high': 0.0}

    # Retrieve and convert form data
    try:
        age = float(request.form['age'])
        tsh = float(request.form['tsh'])
        t3 = float(request.form['t3'])
        t4 = float(request.form['t4'])
        nodulesize = float(request.form['nodulesize'])
        gender = gender_map[request.form['gender'].lower()]
        fhistory = yesno_map[request.form['fhistory'].lower()]
        rexposer = yesno_map[request.form['rexposer'].lower()]
        iodind = yesno_map[request.form['iodind'].lower()]
        smoking = yesno_map[request.form['smoking'].lower()]
        obesity = yesno_map[request.form['obesity'].lower()]
        diabetes = yesno_map[request.form['diabetes'].lower()]
        rlevel = rlevel_map[request.form['rlevel'].lower()]
    except (KeyError, ValueError) as e:
        return f"Input error: {e}", 400

    # Model prediction
    newob = [[age,tsh,t3,t4,nodulesize,gender,fhistory,rexposer,iodind,smoking,obesity,diabetes,rlevel]]
    print(newob)
    model = makeprediction()
    yp = model.predict(np.array(newob))

    if yp[0] == 1:
        result_label = "Malignant"
        explanation = "The prediction indicates a high likelihood of malignant thyroid cancer. Immediate medical evaluation is recommended."
        advice = "It is strongly advised to consult an oncologist or an endocrinologist immediately for further diagnosis and treatment."
    
    else:
        result_label = "Benign"
        explanation = "The prediction suggests that the thyroid condition is most likely benign and non-cancerous."
        advice = "While this condition is not cancerous, regular follow-ups and monitoring are recommended to ensure continued health."

    return render_template('prediction.html', data=result_label, message=explanation, advice=advice)
    
if __name__ == '__main__':
    app.run(debug=True)