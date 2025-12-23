import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/posts/<int:post_id>")
def get_post_data(post_id, get_data_abstraction=requests.get):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

        response = get_data_abstraction(url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
