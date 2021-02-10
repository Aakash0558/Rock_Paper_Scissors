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
game_images = [rock, paper, scissors]
print("Welcome to Rock, Papers, Scissors game!")
user_sign = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

user = int(user_sign)
rock1 = 0
paper1 = 1
scissors1 = 2

if user == rock1:
  print(f"You chose: {game_images[user]}")
elif user == paper1:
  print(f"You chose: {game_images[user]}")
elif user == scissors1:
  print(f"You chose: {game_images[user]}")
elif user >=3 or user <0:
  print("Wrong input")

cpu_input = random.randint(0, 2)

if user < 3 and user >= 0:
  print("CPU chose:")

if ((user <3 and user >=0) and cpu_input == 0):
  print(rock)
elif ((user <3 and user >=0) and cpu_input == 1):
  print(paper)
elif ((user <3 and user >=0) and cpu_input == 2):
  print(scissors)

row1 = ["It's a draw!", "You lose", "You win!!!"]
row2 = ["You win!!!", "It's a draw!", "You lose"] 
row3 = ["You lose", "You win!!!", "It's a draw!"] 
results_list = [row1, row2, row3]

if ((user <3 and user >= 0) and cpu_input <3):
  print(results_list[user][cpu_input])
else: 
  print(" ")
