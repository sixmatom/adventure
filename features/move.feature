Feature: User wants to move to another room

Scenario Outline: Switching rooms
Given The user wants to move from one room to the next
When The user types in the correct input ('ga' + Destination)
And There is a path from the user's Location to Destination
Then The user moves to the next room

| Location | Destination | 
| keuken   | hal         | 
| hal      | keuken      |
| hal      | woonkamer   |