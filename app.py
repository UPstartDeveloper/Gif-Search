from flask import Flask, render_template, request
import requests
import json
import ast
from pprint import pprint

app = Flask(__name__)

# lines inspired by https://tenor.com/gifapi/documentation#quickstart-search
api_key = "EDBOKVM2ES41"  # stores the API key
limit = 10  # number of search results


@app.route('/')
def index():
    """
    Return home page.
    Input: URL request
    Output: renders data using index.html
    """

    # Enables top trends GIFs to show
    if request.args.get('trending'):
        gif_type = ''
        gif_info = get_gif_info(
            gif_type, "https://api.tenor.com/v1/trending?key=%s&limit=%s")
    return render_template("index.html", gif_info=gif_info, gif_type=gif_type)

    gif_type = request.args.get('gif_type')
    if gif_type is None:
        gif_type = ''

    gif_info = get_gif_info(
            gif_type, "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s")
    return render_template("index.html", gif_info=gif_info, gif_type=gif_type)


def get_gif_info(gif_type, api_link):
    """
    A function to dislay search results.
    Input: gif_type, a string storing user's search query
    Output: a list of the URL links to 10 GIF images
    """
    r = ""
    if 'trending' in api_link:
        r = requests.get(
            api_link %
            (api_key, limit))
    else:
        r = requests.get(
            api_link %
            (gif_type, api_key, limit))
    gif_info = []
    if r.status_code == 200:
        # Use JSON from content to get URLs
        json_content = r.json()
        json_results = json_content['results']
        for json_result in json_results:
            gif_info.append(
                {'id': json_result['id'],
                 'itemurl': json_result['itemurl'],
                 'url': json_result['media'][0]['mediumgif']['url']})
        return gif_info
    else:
        # Current bug
        top_ten = None
    return gif_info


if __name__ == '__main__':
    app.run(debug=True)
