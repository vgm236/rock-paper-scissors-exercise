# game.py

#IMPORTS

import random

#INTRODUCTION

print("Rock, Paper, Scissors, Shoot!")

print(" ")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper' or 'scissors' (without the quotes)  ")

print("------------------")
print("You chose:", user_choice)

print(" ")

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("Invalid selection. Please, try again")
    exit() 

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(options)

print("------------------")
print(" ")

print("Generating...")

print(" ") 

print("Computer chose:", computer_choice)

print(" ")

# DETERMINE THE WINNER
  ### rock beats scissors, paper beats rock and scissors beat paper
  ### or same is a tie

if user_choice == computer_choice:
    print("Tie!")


elif user_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")



elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Computer wins!")



elif user_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")


# DISPLAY FINAL OUTPUTS / OUTCOMES

