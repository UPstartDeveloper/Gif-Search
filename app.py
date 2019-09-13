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
    """Return home page."""
    gif_type = request.args.get('gif_type')
    if (gif_type is None):
        gif_type = ''
    gif_list = get_gifs(gif_type)
    return render_template("index.html", gif_list=gif_list, gif_type=gif_type)


def get_gifs(gif_type):
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
        (gif_type, api_key, limit))

    gif_links = []

    if r.status_code == 200:
        # Use JSON from content to get URLs
        content_json = r.json()
        results_json = content_json['results']
        for result in results_json:
            gif_links.append(result['media'][0]['mediumgif']['url'])
        return gif_links
    else:
        # Current bug

        top_ten = None

'''
def top_ten():
    """
    Returns the top ten trending GIFs on Tenor.
    """
    default_locale = requests.get(  # take top 10 trending from default locale
        "https://api.tenor.com/v1/trending?key=%s&limit=%s" % (api_key, limit))

    if default_locale == 200:
        trending = json.loads(default_locale.content)
    else:
        trending = None

    # load the results
    return render_template()
'''

if __name__ == '__main__':
    app.run(debug=True)
