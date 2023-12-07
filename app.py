from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)
@app.route("/", methods =["GET","POST"])
def Index():
    return render_template("index.html")

@app.route('/Summarize', methods=['GET','POST'])
def Summarize():
    if request.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}
        
        data=request.form["textdata"]
        
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        minL = 1
        maxL = int(request.form["maxL"])
        output = query({
            "inputs": data,
            "parameters":{"min_length": minL, "max_length":maxL}      
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")
