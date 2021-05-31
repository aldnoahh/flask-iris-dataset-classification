from flask import Flask, render_template, request, redirect, url_for
from sklearn.externals import joblib

app = Flask(__name__)

flo = joblib.load("/home/analizer/mysite/flower.pkl" , mmap_mode ='r')

@app.route('/',methods=["POST","GET"])

def pred():
    if request.method=="POST":
        f1=request.form["fname"]
        print(f1)
        f0=list(f1.split(','))
        f01= [f0]
        predict=flo.predict_proba(f01)
        for i in predict:
            if i[0]==1:
                result= 'setosa'
            if i[1]==1:
                result= 'versicolor'
            if i[2]==1:
                result= 'virginica'
        print(result)
        return redirect(url_for("user",usr=result))
    else:
        return render_template("pred.html")

@app.errorhandler(500) # Server error
def error1(error):
   return render_template('500.html'), 500

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"