#Number Guessing Game Objectives:
from art import logo
import random
from replit import clear



# Allow the player to submit a guess for a number between 1 and 100.

def choose_level():
  global invalid_level
  difficulty = input("Before we start, what difficulty would you like - easy or hard? For easy 🥸, type 'easy' for hard 🥵, type 'hard'. Goodluck! 🎊🎉  ").lower().strip()

  if difficulty == 'easy':
    invalid_level = True
    return 'easy'
  elif difficulty == 'hard':
    invalid_level = True  
    return 'hard'
  else: # != 'easy' or choose_level() != 'hard':
    print("Please enter a valid difficulty. 👀  :  ")
    invalid_level = False

invalid_level = False
game_over = False

def continue_game():
  global invalid_level
  global game_over
  clear()
  random_number = random.randint(1,100)

  while game_over is not True:
  #Welcome the player to the game using ASCII art and a nice welcome message. Player has to choose a difficulty.   
    print(logo)
    print("Welcome to Johnsons' Number Guessing Game!\n I'm thinking of a number between 1 and 100. Can you guess it? ")
    print(f"Pssst the number is {random_number}.")

  #Create a while loop condition to ensure that a valid difficulty is chosen. This is to avoid an error being produced and 
    while invalid_level is not True:
      level = choose_level()
      if level == 'easy':
        lives = 10
      elif level == 'hard':
        lives = 5

    else:
      print(f"You have {lives} attempts remaining to guess the number.") 
    stil_play = True 
    while stil_play is True:   
      user_guess = int(input("Make a guess: "))
      if lives > 1 and user_guess != random_number:
        if user_guess > random_number:
          print("Too high.")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number.")
        elif user_guess < random_number:
          print("Too low.")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number.")
      elif lives >= 1 and user_guess == random_number:
        print("You win! 🤯")
        stil_play = False
        game_over = True
      else:
        print("You've run out of guesses. You lose. 😭 ")
        stil_play = False
        game_over = True
  if game_over is True:
    play_again = input("Would you like to play again? Y for yes or N for no. 🤓  ").lower().strip()
    if play_again == 'y':
      invalid_level = False
      game_over = False 
      continue_game()
    elif play_again == 'n':
      game_over = True

continue_game()
