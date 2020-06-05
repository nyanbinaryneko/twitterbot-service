import os
from flask import Flask
from kvlty import bot

app = Flask(__name__)

@app.route('/')
def index():
    t = bot.run()
    print(t)
    return f"Kvlt-a-tron in boxes - {t}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
