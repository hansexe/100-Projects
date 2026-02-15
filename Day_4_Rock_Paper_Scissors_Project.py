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

random_int = random.randint(0, 2)

number_chossen_byuser = int(input("Chose the number between 0 for rock, 1 for paper, and 2 for scissors. "))
if number_chossen_byuser == 0:
    print("You choose")
    print(rock)
elif number_chossen_byuser == 1:
    print("You choose")
    print(paper)
else:
    print("You choose")
    print(scissors)

if random_int == 0 and number_chossen_byuser == 2:
    print("Computer choose")
    print(rock)
    print("You lost")
if random_int == 0 and number_chossen_byuser == 1:
    print("Computer choose")
    print(rock)
    print("You won")
if random_int == 0 and number_chossen_byuser == 0:
    print("Computer choose")
    print(rock)
    print("Draw")
if random_int == 1 and number_chossen_byuser == 0:
    print("Computer choose")
    print(paper)
    print("You lost")
if random_int == 1 and number_chossen_byuser == 2:
    print("Computer choose")
    print(paper)
    print("You won")
if random_int == 1 and number_chossen_byuser == 1:
    print("Computer choose")
    print(paper)
    print("Draw")
if random_int == 2 and number_chossen_byuser == 1:
    print("Computer choose")
    print(scissors)
    print("You lost")
if random_int == 2 and number_chossen_byuser == 0:
    print("Computer choose")
    print(scissors)
    print("You won")
if random_int == 2 and number_chossen_byuser == 2:
    print("Computer choose")
    print(scissors)
    print("Draw")
