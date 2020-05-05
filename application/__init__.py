from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/indexfundpredict", methods=['GET', 'POST'])
def indexfundpredict():
   
    # extract form inputs 
    fund = request.form.get("fund")
    
    #url for irisservice
    #url = "http://localhost:5000/api"
    url = "https://index-fund-predictor.herokuapp.com/api"

    #create json from form inputs
    data = json.dumps({"fund": fund})

    #post json to url
    results =  requests.post(url,data)

    possibililty = float(results.content.decode('UTF-8'))
    pred = '0';
    if possibililty >= 0.5:
        pred = '1';
    
    #send features and prediction result to index.html for display
    return render_template("index.html", fund=fund, results=pred)
  