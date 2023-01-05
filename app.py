from flask import *
import pickle
#import mysql.connector as sql
#db=sql.connect(user="root",host="localhost",password="964114",database="NIF")
#cursor= db.cursor()

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('input.html')
@app.route("/add", methods = ['POST'])
def predict():
    if request.method == 'POST':
        pred=0
        N = float(request.form['fn1'])
        P = float(request.form['fn2'])
        K= float(request.form['fn3'])
        temperature = float(request.form['fn4'])
        humidity = float(request.form['fn5'])
        ph = float(request.form['fn6'])
        rainfall = float(request.form['fn7'])
        if N==0 or P==0 or K==0 or temperature==0 or humidity==0 or ph ==0 or rainfall==0:
            return render_template('input.html', results = "KINDLY TRY AGAIN")
        else:
            pred = model.predict([[N, P, K, temperature,humidity,ph,rainfall]])
            pred = str(pred[0])
            #qry="insert into dataset values(%d,%d,%d,%d,%d,%d,%d,'%s')"%(N,P,K,temperature,humidity,ph,rainfall,pred)
            #cursor.execute(qry)
            #db.commit()
            return render_template('input.html', results = "You can grow:"+pred)
    else:
        pred=0
        return render_template('input.html')

if __name__ == "__main__":
    app.run(debug = True)