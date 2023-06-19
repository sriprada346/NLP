from flask import Flask,render_template,request
from io import StringIO
from program import nlp_fun


app = Flask(__name__)


@app.route('/' ,methods=["POST","GET"])
def index():
    return render_template('index.html')

@app.route('/hub', methods=["POST","GET"])
def ind():
    
    x = request.form['hello']
    buffer = StringIO()
    output = nlp_fun(x,buffer)
    return render_template('index.html',output=output)
    

    

if (__name__) =='__main__':
    app.route(debug=True)






