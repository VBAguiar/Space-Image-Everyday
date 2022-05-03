import requests
from flask import Flask, render_template

URL = 'https://api.nasa.gov/planetary/apod?api_key=3wjeWm3ZOtHLswigCfTJ3fhIdELy3zHTfScbwqmM'

def imageURL(URL):
  res = requests.get(URL)

  if res:
    print('Response OK')
  else:
    print('Response Failed')

  text = dict(res.json())
  return text['url']

app = Flask(__name__)

@app.route('/')
def index():
  image = imageURL(URL)
  return render_template('index.html', image=image)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080', debug=True)