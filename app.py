import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/posts/<int:post_id>')
def get_post_data(post_id):
    """
    Fetch post data from external API.

    This is the 'untestable' code we'll refactor in our article.
    It directly calls an external API making it impossible to test
    without real API calls.
    """
    # Direct API call - this is what makes it "untestable"
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)