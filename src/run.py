from src.app import Flask, app

__author__ = 'jushitaa'

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4992)