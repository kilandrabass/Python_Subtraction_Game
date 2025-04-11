"""
    Name: Kilandra Bass
    Collaborators: 
    COSC-010
    Subtraction Game Assignment

    In this game, the user selects an integer between 10 and 30. This
    number represents the starting number of matches. The user and the
    then alternate removing 1 or 2 matches. The object of the game is 
    to avoid removing the last match. The computer will play without
    much strategy, generally just choosing 1 or 2 at random.
"""
import random
import time

def play_game():
  delay = 1

  print("Welcome to the Subtraction Game!")

  while True:
      try:
          n = int(input("Enter the starting number of matches (between 10 and 30): "))
          if 10 <= n <= 30:
              break
          else:
              print("Please enter a number between 10 and 30.")
      except ValueError:
          print("Invalid input. Please enter a valid number.")

  remaining = n

  while remaining > 0:
      # User's turn
      while True:
          try:
              userChoice = int(input("How many matches do you want to remove? (1 or 2): "))
              if userChoice in [1, 2] and userChoice <= remaining:
                  break
              else:
                  print("Invalid input. Please choose 1 or 2 matches and make sure it's available.")
          except ValueError:
              print("Invalid input. Please enter a valid number.")

      remaining -= userChoice
      print("...And of the original", n, "matches, now there are", remaining, "left")

      # Check if user won
      if remaining == 0:
          print("Congratulations! You won!")
          break

      # Computer's turn
      time.sleep(delay * 2)
      computerChoice = random.choice([1, 2])
      remaining -= computerChoice
      print("...The computer chooses", computerChoice)
      print("...And of the original", n, "matches, now there are", remaining, "left")

      # Check if computer won
      if remaining <= 0:
          print("Sorry, the computer won!")
          break

  while True:
      play_again = input("Do you want to play again? (yes/no): ").lower()
      if play_again in ['yes', 'no']:
          break
      else:
          print("Invalid input. Please enter 'yes' or 'no'.")

  return play_again == "yes"

# Main loop for the game
while True:
  if not play_game():
      print("Thanks for playing. Goodbye!")
      break