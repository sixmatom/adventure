from behave import given, when, then  # pylint: disable=no-name-in-module

from game import Game

@given(u'the user starts the game')
@when(u'the user types the correct path python shell.py {game.json:d}')
@then(u'the games should load the correct json file')