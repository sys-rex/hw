from flask import Flask
#import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world HW py prod!!!"

if __name__ == "__main__":
 #   port = int(os.environ.get("PORT", 5010))
    app.run(debug=True, host='0.0.0.0')


# from time import sleep

# while True:
#     print("Hello world")
#     sleep(1)
