from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template('predict.html')

@app.route('/predict', methods = ['POST'])
def fun2():
    name=request.form['ename']
    exp = float(request.form['yrsexp'])
    model = pickle.load(open('sal_model.pkl', 'rb'))
    sal = model.predict([[exp]])
    return '<h1>Thanks for visiting us. Your Expected Salary is {} </h1>'.format(int(sal[0]))

@app.route('/contactus')
def fun3():
    return 'Thanks for visiting contact us'

if __name__=='__main__':
    app.run(debug = True)