from app import app
from flask import render_template, request
from models.game import *
from models.player import Player

@app.route("/")
def index():
    return "TESTING"

@app.route("/<player1_choice>/<player2_choice>")
def play_game(player1_choice, player2_choice):
    player1 = Player("Louise", player1_choice)
    player2 = Player("Simona", player2_choice)

    game = Game()

    winner = game.win_game(player1, player2)
    
    return render_template("game.html", title="Results", player1=player1, player2=player2, winner=winner)

@app.route("/home")
def rule_page():
    return render_template("home.html", title="Home Page")

