from random import randint
def rockpaperscissor():
    choices = {1:"Rock" ,2:"Paper" , 3:"Scissors" , 4:"Exit"}
    score=0
    attempts = 0
    while True:
        try:
            user_choice = int(input("Press 1 for Rock , 2 for Scissors , 3 for Paper and 4 to exit"))
            if user_choice == 4:
              break
            if user_choice not in {1, 2, 3}:
                print("Pls choose a number between 1 and 4 inclusive.")
                continue

            computer_choice = randint(1,3)

            if user_choice == computer_choice:
                print("its a draw")

            elif str(user_choice) + str(computer_choice) in ["13", "21", "32"]:
                print("You Win!")
                score += 1

            elif str(user_choice) + str(computer_choice) in ["12", "23", "31"]:
                print("You Loose")
                score -= 1

            attempts += 1

        except:
            print("Invalid choice.")
            break

    print(f"Your score is {score}/{attempts}")
    print("Thanks for playing.")

rockpaperscissor()











