import requests
from flask import Flask, render_template, request

app = Flask(__name__)

URL_LOCATION = "https://us1.locationiq.com/v1/search.php"

PRIVATE_TOKEN = "pk.63773c9810c6728d01e8c90ebcc93ff7"


def geo_my_location(ADDRESS):
    """
    Takes in json does magic spits out a dict 
    """
    data = {
        'key': PRIVATE_TOKEN,
        'q': ADDRESS,
        'format': 'json'
    }
    response = requests.get(URL_LOCATION, params=data)
    res1 = {}
    res1['Latitude'] = response.json()[0]['lat']
    res1['Longitude'] = response.json()[0]['lon']
    return res1


@app.route('/')
def index():
    """
    home html
    """
    return render_template('index.html')


@app.route("/address", methods=['GET', 'POST'])
def address_():
    """
    address result html
    """
    res = request.args.get("address")
    result_address = geo_my_location(res)
    return render_template("result.html", geo_my_location=True, result_address=result_address)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
