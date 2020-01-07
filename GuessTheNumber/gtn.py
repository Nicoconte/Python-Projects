import random
def menu():
    print()
    print("*********************************************")
    print("***          GUESS THE NUMBER             ***")
    print("*********************************************")

def restart(score,name):
    confir = input("Do you want to quit/restart? ")
    if confir == "yes":
        return  main(score,name)
    elif confir == "no":
        print("Score ",score,"\n","Name ",name) #Let´s try to show the score with dic
        print("Bye ",exit())
    else:
        print("Invalid command", restart(score,name))

def main(score,name):
    menu()
    user_name = input("What´s your name ")
    number = random.randint(0,100)
    cont = 0
    try:
        user_input = int(input("> "))
        while user_input != -1: #Main loop
            if user_input < number:
                print("The number is pretty down")
            elif user_input > number:
                print("It´s too high")
            else:
                print("Correct! You win ",user_name)
                score.append(cont)
                name.append(user_name)
                return restart(score,name)
            cont = cont + 1
            user_input = int(input("> "))
    except ValueError:
            print("Input must be a number, let´s begin again")
            main(score,name)
    print("You quit :( (you lose all your progress until now)")
    restart(score,name) #We´ll restart the game if we put -1 in the input

#Global variable
score = []
name = []

#Main program
main(score,name)
