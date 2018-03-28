
import flask
from flask import Flask, render_template
from sklearn.externals import joblib


app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/predict",methods=['POST'])


def index():
   return flask.render_template('index.html')


def rediction():
	if request.method=='POST':
		return render_template('index.html',label="3")


if __name__ == '__main__':
	model=joblib.load('svm.pkl')
	app.run(host='0.0.0.0', port=8000, debug=True)
