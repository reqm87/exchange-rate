from flask import Flask


app = Flask(__name__)


@app.route("/")
def exchange_rate():
    return "Exchange rate is working!"


if __name__ == "__main__":
    app.run(debug=True)
