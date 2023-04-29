"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/player/verify')
def verify_player():
    """Show site on which an player can verify the profile"""
    return render_template("verify_player.html")


@app.route('/player/create')
def create_player():
    """Show site on which an admin can create a new player"""
    return render_template("create_player.html")


@app.route('/player/edit')
def edit_player_profile():
    """Show site on which user can edit preferences"""
    return render_template("edit_player.html")


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
