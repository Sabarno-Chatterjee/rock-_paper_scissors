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

#Write your code below this line 👇
comp = random.randint(1, 3)
print(comp)
user = input("Please enter 1 for rock, 2 for paper or 3 for scissor\n")
user = int(user)
if (comp == 1 or comp == 3) and (user == 3 or user == 1):
    print("Rock wins over scissor.")
elif (comp == 2 or comp == 1) and (user == 1 or user == 2):
    print("Paper wins over rock.")
elif (comp == 3 or comp == 2) and (user == 2 or user == 3):
    print("Scissor wins over paper.")
elif comp == user:
    print("Draw.")
'''
else:
    print("Invalid input, run the game again!")
'''