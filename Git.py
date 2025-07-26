import random

Rock = '''
───────
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
────────
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
────────────
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]

while True:
    try:
        user_choice = int(input("\nWhat do you choose buddy? 0 for Rock, 1 for Paper, and 2 for Scissors: "))
        if user_choice not in [0, 1, 2]:
            print("Abey 0, 1, ya 2 mese choose kar:.. You lose")
            continue
        print("You chose:")
        print(game_images[user_choice])
    except ValueError:
        print("Please enter a number (0, 1, or 2).")
        continue

    comp_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[comp_choice])

    if user_choice == comp_choice:
        print("Nobody won")
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print("You win")
    else:
        print("You lose")

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("Okay buddy, game over. See you next time!")
        print("Thanks for playing!")
        break
