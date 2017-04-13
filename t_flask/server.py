import os
from flask import Flask, render_template, request

app = Flask(__name__)

# root page
@app.route("/")
def index():
    return render_template("index.html")

# html form demo input page
@app.route("/form")
def form():
    return render_template("form.html")

# html form demo result page
@app.route("/result", methods = ["GET", "POST"])
def result():
    if request.method == "POST":
        r_first = request.form.get("first")
        r_middle = request.form.get("middle")
        r_last = request.form.get("last")
    if request.method == "GET":
        r_first = request.args.get("first")
        r_middle = request.args.get("middle")
        r_last = request.args.get("last")
    return render_template("result.html", first=r_first, middle=r_middle, last=r_last)

# configure server
server_address = "0.0.0.0"
port_number = 8080

# run server
if __name__ == "__main__":
    app.run(host = os.getenv('IP', server_address), 
            port = int(os.getenv('PORT', port_number)))