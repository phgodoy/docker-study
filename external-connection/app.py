import flask
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    random_user_api_response = requests.get('https://randomuser.me/api')
    random_user_data = random_user_api_response.json()
    return flask.jsonify(random_user_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)