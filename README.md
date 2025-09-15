# Enterprise-SW-Plat-Assignment-1

To complete the 2nd and 3rd part of this assignment, I made a hangman game using flask and hosted it locally on a docker container.

## I created a Dockerfile as seen in the repo above. And ran:

docker build -t bolt162/hangman:latest

<img width="1260" height="618" alt="Screenshot 2025-09-14 at 1 53 56 PM" src="https://github.com/user-attachments/assets/88ababa2-f0f4-4a8d-a5fe-98534e911f31" />


## Option 1: Ubuntu packages

    sudo apt-get install python-flask python-flask-sqlalchemy

## Option 2: pip

[Install pip](https://pip.pypa.io/en/stable/installing/), then:

    pip install Flask Flask-SQLAlchemy

# Run

    python hangman.py

Create dabase with:

    python -c 'from hangman import db; db.create_all()'

# Links

* Hangman github repository: https://github.com/vlopezferrando/hangman
* Slides: https://slides.com/victorlf/flask
* Flask: http://flask.pocoo.org
* Jinja2: http://jinja.pocoo.org/docs/dev/
* Bootstrap: http://getbootstrap.com
* JQuery: https://jquery.com
