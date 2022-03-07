# TDD Exercise

## Learning Goals 
- Practice identifying test cases
- Practice writing tests with pytest
- Practice the Test Driven Development (TDD) programming workflow

## About BlackJack

In this exercise we will write a method and set of tests in TDD fashion which calculates a hand's BlackJack score.

In the card game BlackJack each card has a value.
-  Number cards (2-10) carry the card's numeric value.
-  Face cards on the other hand ("Jack", "Queen", "King") have a value of 10.
-  Aces (1) can have a value of either 1 or 11, whichever will get the hand closest to 21 without going over.

For example if I had a 3, a King, and an Ace, my BlackJack score is 14 (3 + 10 + 1).  If I have an Ace, and a Jack then my score is 21 (11 + 10).

A hand, an array of Card values, must be between 2 and 5 items inclusive.

When a hand's score is greater than 21, the hand is a **bust** and the player automatically loses.

## Problem Set

### Part 1:  Identifying Edge & Nominal Cases

Identify some of the following tests cases

- At least two nominal cases
- At least three edge cases

## Classroom activity

### Part 2:  Identifying Edge & Nominal Cases

In class, you will:

1. Review the test cases you identified in Part 1
1. Determine how you would test these cases

### Part 3:  Calculating a Score

We will write a method called:  `blackjack_score` which take a list of card values and returns the blackjack score.  The card values can be any of the following, number values 2-10, "King", "Queen", "Jack", and "Ace". For example `blackjack_score(["Ace", 5, 3])` will return 19. If the list contains an invalid card value or the hand contains more than 5 cards, return `"Invalid"`. If the total exceeds 21, return `"Bust"`.  

*Note: These last two cases may be better handled by raising an exception (as opposed to returning `"Invalid"` and `"Bust"`).We can consider that when we learn more about raising exception.*

In this exercise we will complete the given tests in `test_blacjack_score.py` and updating the `blackjack_score` function in `main.py` to make it pass.

- Step 1:  Complete the given test
- Step 2:  Update `blackjack_score` to pass the test (Run the replit from `main.py` to see the test result(s)).
- Step 3:  Move to the next test

We will likely not have time to write every test and implement every piece of code to implement a complete `blackjack_score` function. Keep in mind that the learning goals for this activity are to practice identifying test cases, practice writing tests with pytest, and practice working in a TDD fashion.

**Follow classroom instructions on how to set-up the replit for collaboration.**

