import os
from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View

# nav = Nav()
# topbar = Navbar('',
#                 View('avaren', 'index'),
#                 View('precipice ep', 'index')
#                 )

# Register topnav
# nav.register_element('top', topbar)

app = Flask(__name__)
# nav.init_app(app)


@app.route("/")
def index():
    return render_template("index.html",
                           title="avaren music",
                           active='home')


@app.route("/precipice-ep/")
def precipice_page():
    return render_template("precipice-ep.html", active='precipice-ep')


@app.route("/demos/")
def demos():
    return render_template("demos.html", active='demos')


@app.route("/mixes/")
def mixes():
    return render_template("mixes.html", active='mixes')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
