from flask import Flask, render_template, request
import requests
import json
import ast
from pprint import pprint

app = Flask(__name__)

# lines inspired by https://tenor.com/gifapi/documentation#quickstart-search
# set the API key and limit for search result
api_key = "EDBOKVM2ES41"
limit = 10  # number of search results


@app.route('/')
def index():
    """Return homepage."""
    msg = 'GIF SEARCH!'
    return render_template("index.html", msg=msg)


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
        top_ten = None

@app.route('/getGif')
def get_gif():
    gif_type = request.args.get('gif_type')
    gif_list = get_gifs(gif_type)
    displayString = ""
    for link in gif_list:
        displayString += link + '<br>'
    return render_template('results.html', gif_list=gif_list, gif_type=gif_type, link=link)

if __name__ == '__main__':
    app.run(debug=True)
