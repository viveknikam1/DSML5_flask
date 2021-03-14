from flask import Flask, render_template, request
import pickle
app1 = Flask(__name__)

@app1.route('/')
def fun1():
    return render_template('predict.html')

@app1.route('/predict', methods = ['POST'])
def fun2():
    name=request.form['ename']
    exp = float(request.form['yrsexp'])
    model = pickle.load(open('sal_model.pkl', 'rb'))
    sal = model.predict([[exp]])
    return '<h1>Thanks for visiting us. Your Expected Salary is {} </h1>'.format(int(sal[0]))

@app1.route('/contactus')
def fun3():
    return 'Thanks for visiting contact us'

if __name__=='__main__':
    app1.run(debug = True)
