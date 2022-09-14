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
game = [rock,paper,scissors]

user= int(input("Please enter 0 for rock, 1 for paper or 2 for scissors.\n"))
if user >= 3 or user < 0:
    print("Invalid input, you lose!")
else:
    print(game[user])
    comp= random.randint(0,2)
    print("Computer chose:\n")
    print(game[comp])

#if  user >= 3 or user < 0:
#   print("Invalid input, you lose!")
    if user == 0 and comp == 2:
        print("You win!")
    elif user == 2 and comp == 0:
        print("You lose!")
    elif comp > user:
        print("You lose!")
    elif user > comp:
        print("You win!")
    elif comp == user:
        print("It's a draw.")



