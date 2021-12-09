from flask import Flask
from data_handler import adding_values

app = Flask(__name__)

@app.route("/")
def index():
    a=6
    b=6
    c=adding_values(a,b)
    return f"que pedoski {c}"
if __name__=="__main__":
    app.run(debug=True)