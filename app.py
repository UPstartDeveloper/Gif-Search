from flask import Flask, render_template, request
import requests
import json
import ast

app = Flask(__name__)

# lines inspired by https://tenor.com/gifapi/documentation#quickstart-search
# set the API key and limit for search result
api_key = "EDBOKVM2ES41"
limit = 10  # number of search results

# test search term
search_term = "happiness"

r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
    (search_term, api_key, limit))

gif_links = []

if r.status_code == 200:
    # load the GIFs using the urls for smaller GIF sizes
    content = str(r.content)

    while len(gif_links) < 10:
        starting_content_index = content.find('"mediumgif"')
        content = content[starting_content_index:]
        starting_content_index = content.find('"url"')
        gif_link = content[starting_content_index + 8: content.find(',') - 1]
        gif_links.append(gif_link)
        content = content[content.find(',') - 1:]

    r.close()

    for link in gif_links:
        print(link)
   
else:
    top_ten = None




# @app.route('/')
# def index():
#     """Return homepage."""
#     return "Hello there user!"
#     # TODO: Extract query term from url

#     # TODO: Make 'params' dict with query term and API key

#     # TODO: Make an API call to Tenor using the 'requests' library

#     # TODO: Get the first 10 results from the search results

#     # TODO: Render the 'index.html' template, passing the gifs
#     # as a named parameter
#     # msg = 'GIF SEARCH!'
#     # return render_template("index.html", msg = msg)

# @app.route('/getGif')
# def get_gif():
#     gif_type = request.args.get('gif_type')
#     return 'The gif type you\'ve requested is ' + gif_type


# if __name__ == '__main__':
#     app.run(debug=True)
