from distutils.log import debug
from turtle import speed
from flask import Flask, render_template, request
import joblib


app = Flask(__name__)

#Loading model
model = joblib.load('linermodel_ev_temp.pkl')

@app.route('/')
def welcome():
    return render_template('Landingpage.html')

@app.route('/submit', methods=['POST'])
def Result():
    
    a0 = request.form.get('Ambient temp')
    a1 = request.form.get('Coolant_temp')
    a2 = request.form.get('Current_d_component')
    a3 = request.form.get('Current_q_component')
    a4 = request.form.get('Motor_speed')
    a5 = request.form.get('Permanent_magnet')
    a6 = request.form.get('Motor_torque')
    a7 = request.form.get('Voltage_d1')
    a8 = request.form.get('Voltage_q1')

    print(a0)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    print(a8)
    #input_11 = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
    #input_final = np.array(input_11)
    result1 = model.predict([[a0, a1, a2, a3, a4, a5, a6, a7, a8]])
    print(result1)

    #if result1 < 35:
        #result1 = result1,"The temperature is under controlled"
    #else:
        #result1 = result1, "Temperature is high please trun on coolant"
    return render_template('prediction_page.html', output = result1)

if __name__ == "__main__":
    app.run(debug = True)