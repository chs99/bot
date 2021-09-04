from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

#to run web server
def run():
  app.run(host='0.0.0.0',port=8080)

#defining keep alive function
def keep_alive():
    t = Thread(target=run)
    t.start()