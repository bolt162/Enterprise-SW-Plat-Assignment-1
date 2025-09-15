# Enterprise-SW-Plat-Assignment-1

To complete the 2nd and 3rd part of this assignment, I made a hangman game using flask and hosted it locally on a docker container.

# Part #2

## I created a Dockerfile as seen in the repo above and built the docker image using:

docker build -t bolt162/hangman:latest .

<img width="1260" height="618" alt="Screenshot 2025-09-14 at 1 53 56 PM" src="https://github.com/user-attachments/assets/88ababa2-f0f4-4a8d-a5fe-98534e911f31" />


## The second step was to write down unit tests and run them to ensure that the game does not have edge cases where the applicaiton would crash. The test files are available in the tests/ repository and I ran the following command to run those tests:

docker run —rm bolt162/hangman: latest python -m unittest discover -s tests

<img width="1279" height="130" alt="Screenshot 2025-09-14 at 1 59 35 PM" src="https://github.com/user-attachments/assets/62b4706c-6624-44be-a134-7ddecf4f8bb2" />


## The last step was to push the image to the registry with:

docker push bolt162/hangman:latest

<img width="774" height="229" alt="Screenshot 2025-09-14 at 2 05 46 PM" src="https://github.com/user-attachments/assets/f37834cb-a6a1-4670-a81e-00700f3da3af" />

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
