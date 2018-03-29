import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
	if request.method=='POST':

		# get uploaded image file if it exists
		text=[]
		txt = request.form['text']
		text.append(txt)

		
		prediction = svm.predict(text)
		label=prediction
	
		return render_template('index.html', label=label)


if __name__ == '__main__':
	svm = joblib.load('svm.pkl')
	app.run(host='0.0.0.0', port=8000, debug=True)