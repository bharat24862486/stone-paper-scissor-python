# # print("hello word")

# import random

# c1=0;
# c2=0;

# flag=True

# def winner(player_choice,computer_choice):
#     if player_choice == computer_choice:
#         return "It's a tie!"
#     elif (
#         (player_choice == 'rock' and computer_choice == 'scissors') or
#         (player_choice == 'paper' and computer_choice == 'rock') or
#         (player_choice == 'scissors' and computer_choice == 'paper')
#     ):
#         return "You win!"
#     else:
#         return "Computer wins!"
    

# def startGame():
#     choices = ['rock','paper','sessor']
#     print("Welcome to Stone, Paper, Scissors!")
#     print("Please choose one of the following options:")
#     print("1. Rock")
#     print("2. Paper")
#     print("3. Scissors")
#     print("4. Quit")


#     player_choice = int(input("Enter your choice (1-3): ")) - 1

#     # if player_choice == 3:

#     #     flag = False

        

        

#     if player_choice < 0 or player_choice >= 3 :
#         print("Invalid input")
#         return 

#     player_value = choices[player_choice]
#     computer_value = random.choice(choices)

#     print("You chose:", player_value)
#     print("Computer chose:", computer_value)

#     winners = winner(player_value,computer_value)

#     print(winners)

# startGame()

# while True:
#     startGame()
#     choice = input("Do you want to play again? (yes/no): ")
#     # if choice.lower() != "yes":
#     #     print("You have successfully quit this game")
        
#     #     print("Your Score is:", c1)
#     #     print("Computer Score is:", c2)

#     #     if c1 > c2 :
#     #        print("You won the game")
           
#     #     elif c1 < c2:
#     #        print("Computer won the game")
           
#     #     else :
#     #        print("Computer and You score same")
           
#     #     break


   
   
   




# import random
# flag = True
# c1=0;
# c2=0;

# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "It's a tie!"
#     elif (
#         (player_choice == 'rock' and computer_choice == 'scissors') or
#         (player_choice == 'paper' and computer_choice == 'rock') or
#         (player_choice == 'scissors' and computer_choice == 'paper')
#     ):
#         # c1+=1;
#         return "You win!"
#     else:
#         # c2+=1;
#         return "Computer wins!"

# def play_game():
#     choices = ['rock', 'paper', 'scissors']
#     print("Welcome to Stone, Paper, Scissors!")
#     print("Please choose one of the following options:")
#     print("1. Rock")
#     print("2. Paper")
#     print("3. Scissors")
#     print("4. Quit")

#     player_choice = int(input("Enter your choice (1-4): ")) - 1

#     if player_choice == 3 :
#         flag = False
#         return

#     if player_choice < 0 or player_choice >= 4:
#         print("Invalid choice. Please try again.")
#         return

#     computer_choice = random.choice(choices)

#     player_choice_text = choices[player_choice]

#     print("You chose:", player_choice_text)
#     print("Computer chose:", computer_choice)

#     winner = determine_winner(player_choice_text, computer_choice)
#     print(winner)

# # play_game()


# if flag:
#     play_game()

# else :
#     print("You have successfully quit this game")
        
#     print("Your Score is:", c1)
#     print("Computer Score is:", c2)

#     if c1 > c2 :
#         print("You won the game")
           
#     elif c1 < c2:
#         print("Computer won the game")
           
#     else :
#         print("Computer and You score same")





import random

flag = True
player_wins = 0
computer_wins = 0


def determine_winner(player_choice, computer_choice):
    global player_wins, computer_wins

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        player_wins += 1
        return "You win!"
    else:
        computer_wins += 1
        return "Computer wins!"


def play_game():
    global flag

    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Stone, Paper, Scissors!")
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice = int(input("Enter your choice (1-4): ")) - 1

    if player_choice == 3:
        flag = False
        return

    if player_choice < 0 or player_choice >= 4:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.choice(choices)

    player_choice_text = choices[player_choice]

    print("You chose:", player_choice_text)
    print("Computer chose:", computer_choice)

    result = determine_winner(player_choice_text, computer_choice)
    print(result)
    print("Player wins:", player_wins)
    print("Computer wins:", computer_wins)


while flag:
    play_game()

print("You have successfully quit the game")
