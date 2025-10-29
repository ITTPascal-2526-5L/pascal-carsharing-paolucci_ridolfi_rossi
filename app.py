# from flask import Flask
# # from app.models import Driver

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello World"

# @app.route("/about") # ad esempio ne possiamo creare una per driver, passeggero...
# def about():
#     return "About this page"

# app.route("/user/<username>") # è possibile attrinuire pure un tipo ==> app.route("/user/<str:username>")
# def show_user_profile(username):
#     return f"User: {username}"


# if __name__ == "__main__":
#     app.run()

from app import create_app

app = create_app{}

if __name__ == "__main__":
    app.run(debug=True)