from flask import Flask

app = Flask(__name__)

@app.route("/")
def add():
    return "Shomurodov_Mirjakhan_2003"

if __name__=="__main__":
    app.run(debug=True,port=4000)