from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
'''
# lines inspired by https://tenor.com/gifapi/documentation#quickstart-search
# set the API key and limit for search result
api_key = "EDBOKVM2ES41"
limit = 10  # number of search results

# test search term
search_term = "excited"

r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
    (search_term, api_key, limit))

if r.status_code == 200:
    # load the GIFs using the urls for smaller GIF sizes
    top_ten = json.load(r.content)
    print(top_ten)
else:
    top_ten = None
'''

@app.route('/')
def index():
    """Return homepage."""
    return "Hello there user!"
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs
    # as a named parameter

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
