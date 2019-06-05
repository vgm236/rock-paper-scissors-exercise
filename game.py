# game.py

#IMPORTS

import random

#INTRODUCTION

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper' or 'scissors' (without the quotes)  ")

print("------------------")
print("You chose:", user_choice)

print(" ")

# VALIDATE INPUTS

if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid selection. Please, try again")
    exit() 

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(["rock", "paper", "scissors"])

print("------------------")
print(" ")

print("Generating...")

print(" ")

print("Computer chose:", computer_choice)

print(" ")

# DETERMINE THE WINNER



# DISPLAY FINAL OUTPUTS / OUTCOMES

