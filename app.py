from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello,flask"

@app.route('/syn')
def syncro():
    with open("file.txt","r") as f:
        data = f.read()
        return data



if __name__ == '__main__':
    app.run(debug=True)