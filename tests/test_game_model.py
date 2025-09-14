import unittest
from hangman import Game, db, app
from flask import Flask

class GameModelTestCase(unittest.TestCase):
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

    def test_game_creation(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        self.assertIsNotNone(game.pk)
        self.assertEqual(game.player, 'tester')
        self.assertTrue(len(game.word) > 0)
        self.assertEqual(game.tried, '')

    def test_try_letter(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        letter = game.word[0]
        game.try_letter(letter)
        self.assertIn(letter, game.tried)

    def test_win_condition(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        for letter in set(game.word):
            game.try_letter(letter)
        self.assertTrue(game.won)
        self.assertFalse(game.lost)
        self.assertTrue(game.finished)

    def test_loss_condition(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        # Try 6 wrong letters
        wrong = [chr(i) for i in range(65, 91) if chr(i) not in game.word][:6]
        for letter in wrong:
            game.try_letter(letter)
        self.assertTrue(game.lost)
        self.assertFalse(game.won)
        self.assertTrue(game.finished)

    def test_points_calculation(self):
        game = Game('tester')
        db.session.add(game)
        db.session.commit()
        # No errors
        for letter in set(game.word):
            game.try_letter(letter)
        points_no_errors = game.points

        # Add errors
        game2 = Game('tester')
        db.session.add(game2)
        db.session.commit()
        wrong = [chr(i) for i in range(65, 91) if chr(i) not in game2.word][:6]
        for letter in wrong:
            game2.try_letter(letter)
        for letter in set(game2.word):
            game2.try_letter(letter)
        self.assertGreater(len(game2.errors), 0)  # Ensure errors exist
        self.assertLess(game2.points, points_no_errors)

if __name__ == '__main__':
    unittest.main()
