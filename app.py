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
    gif_type = request.args.get('gif_type')
    if (gif_type is None):
        gif_type = ''
    gif_info = get_gif_info(gif_type)
    return render_template("index.html", gif_info=gif_info, gif_type=gif_type)


def get_gif_info(gif_type):
    """
    A function to dislay search results.
    Input: gif_type, a string storing user's search query
    Output: a list of the URL links to 10 GIF images
    """
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
        (gif_type, api_key, limit))
    gif_info = []
    if r.status_code == 200:
        # Use JSON from content to get URLs
        json_content = r.json()
        json_results = json_content['results']
        for result in json_results:
            gif_info.append({'id':result['id'], 'itemurl':result['itemurl'], 'url':result['media'][0]['mediumgif']['url']})
            print({'id':result['id'], 'itemurl':result['itemurl'], 'url':result['media'][0]['mediumgif']['url']})
        return gif_info
    else:
        # Current bug
        top_ten = None
    return gif_info

'''
def top_ten():
    """
    Returns the top ten trending GIFs on Tenor.
    Input: user clicks on button on index.html
    Output: a list of 10 URL links to popular GIFs on Tenor.
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
