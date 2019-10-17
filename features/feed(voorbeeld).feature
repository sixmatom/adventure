Feature: Calculate feed

Scenario Outline: feeding a suckler cow
  Given the cow weighs <weight> kg
  And the cow is <age> years
  When we calculate the feeding requirements
  Then the energy should be <energy> MJ
  And the protein should be <protein> kg

  Examples:
    | weight | energy | protein | age |
    |    450 |  26500 |     215 |   0 |
    |    500 |  29500 |     245 |   0 |
    |    575 |  31500 |     255 |   0 |
    |    600 |  37000 |     305 |   0 |
    |    650 |  40000 |     350 |   0 |
    |    650 |  38000 |     333 |   1 |
    |    650 |  36000 |     315 |   2 |
    |    650 |  34000 |     298 |   3 |
    |    650 |  32000 |     280 |   4 |