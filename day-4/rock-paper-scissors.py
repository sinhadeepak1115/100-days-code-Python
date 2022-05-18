import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

 # Players Choice

player_choice = int(input("What do you choose? Type Ø for Rock, 1 for Paper or 2 for Scissors."))
print(game_image[player_choice])

 # Computers Choice
random_int = random.randint(0,2)
print(game_image[random_int])

if random_int == player_choice:
    print("The match is draw.")
elif player_choice == 0 and random_int == 2:
    print("You Win!")
elif player_choice > random_int:
    print("You Win")
elif random_int > player_choice:
    print("You lose!")
elif player_choice > 3:
    print("Please enter a valid input.")
