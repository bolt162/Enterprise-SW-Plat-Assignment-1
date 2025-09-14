import unittest
from hangman import app, db, Game

class HangmanRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'html', response.data)  # crude check for template

    def test_new_game_route(self):
        response = self.app.get('/play?player=tester')
        self.assertEqual(response.status_code, 302)  # should redirect
        self.assertIn('/play/', response.location)

    def test_play_route_get(self):
        # Create a game
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        response = self.app.get(f'/play/{game.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'html', response.data)

    def test_play_route_post(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        response = self.app.post(f'/play/{game.pk}', data={'letter': game.word[0]})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'html', response.data)

if __name__ == '__main__':
    unittest.main()
