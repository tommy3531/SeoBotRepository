from datetime import datetime

from flask import Flask

from slack import RTMClient


app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route('/test', methods=['POST'])
def testpage():
    return"""<h1>Test Page</h1>"""

    url = "https://canssens-seo-extraction-v1.p.rapidapi.com/seo/api/"

    payload = "url=www.mashape.com"
    headers = {
        'x-rapidapi-host': "canssens-seo-extraction-v1.p.rapidapi.com",
        'x-rapidapi-key': "zjgGHjiZ0Xmsh3ZyiBkvbEY02oasp1sLHlojsnOF9ZMrOtFmcA",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)