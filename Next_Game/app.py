from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# Define your RAWG API key here
RAWG_API_KEY = '0a929281a92f4c4782b0b194068a9e88'

@app.route('/')
def random_game():
    # Generate a random page number to retrieve random games
    random_page = random.randint(1, 100)

    # Make a request to the RAWG API to get a list of games
    rawg_url = 'https://api.rawg.io/api/games'
    params = {
        'key': RAWG_API_KEY,
        'page_size': 1,
        'page': random_page,
    }

    response = requests.get(rawg_url, params=params)
    data = response.json()

    if 'results' in data and data['results']:
        game = data['results'][0]
        return render_template('index.html', game=game)
    else:
        return 'No game found'

if __name__ == '__main__':
    app.run(debug=True)
