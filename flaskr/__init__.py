"""
This module contains the entry point to the program
"""
import os

from flask import Flask, jsonify, request, render_template
from flaskr.models.my_app import MyApp
from flaskr.models.sudoku_verifier import SudokuVerifier

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    my_app = MyApp()
    sudokus = my_app.read_input()
    @app.route('/')
    def hello():

        data = {
            'sudokus' : []
        }

        for sudoku in sudokus:

            data['sudokus'].append(my_app.verify_sudoku(sudoku))


        return render_template('home.html', data = data)

    return app
