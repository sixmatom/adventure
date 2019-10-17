Feature: user wants to load the game

Scenario Outline: loading json file
    Given the user starts the game 
    When the user types the correct path ('python shell.py <game.json>')
    Then the games should load the correct json file

    Examples:
    | game.json | Header 2 | Header 3 |
    | data/test_game.json  | Value 2  | Value 3  |