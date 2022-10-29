from flask import Flask, render_template, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def show_game():
    """
    Displays the Game Board
    """
    game_data = boggle_game.make_board()
    session['board']= game_data
    return render_template('game.html', board = game_data)

@app.route('/check_valid_word')
def check_word():
    """
    checks if word is valid
    """
    guess = request.args.get('guess')
    board= session['board']
    result = boggle_game.check_valid_word(board,guess)
    response = jsonify({'result': result})
    return response
