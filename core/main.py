from flask import Flask, jsonify

from provider import banxico, fixer

app = Flask(__name__)


@app.route("/")
def exchange_rate():
    rates = []
    rates.append(fixer())
    rates.append(banxico())
    result = {'rates': rates}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
