from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'
if __name__ == '__main__':
    app.run(debug=True)
#app.run(host='0.0.0.0', port=81)
