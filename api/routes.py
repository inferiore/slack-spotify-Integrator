from flask import Flask, request
from services.spotify import Spotify
app = Flask(__name__)
app.config["DEBUG"]=True
spotify = Spotify()
@app.route('/',methods=["post"])
def webhook():
    spotify.refreshToken()
    data = request.get_json();
    if("edited" in request.get_json()):
        return "editado"
    else:
        if("starting" in data["text"]):
            spotify.pause()
        if ("done" in data["text"]):
            spotify.play()
    return "done"
@app.route('/spotify-login',methods=["get"])
def spotify_login():
    spotify.getToken(request.args.get("code"))
    return "login done :)<br>"


app.run()