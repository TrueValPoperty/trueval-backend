from flask import Flask
from routes.log import log_valuation

app = Flask(__name__)
app.add_url_rule("/log", view_func=log_valuation, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
