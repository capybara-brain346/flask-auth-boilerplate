from flask import Flask, render_template
from auth import auth

main = Flask(__name__)
main.register_blueprint(auth, url_prefix="/auth")


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    main.run(debug=True)
