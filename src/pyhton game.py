from itertools import count


def main():
    print("Welcome to my game")

    player_name=input("what is your name? ")
    print("Hi " + player_name)

    lives = 3
    print(f"You have {lives} lives remaining, make them count!")
    print("You are located in an abandoned laboratory and you must find away to get out" )
    print("To successfully leave the building you must enter 4 other rooms in which you will enntouer puzzles which will be rquired towards the end of the game" )
    

    print("You notice a door ahead of you which looks to be pried open")

    print("To move towards the enter North")
    direction =input("Which direction do you want to go? ")
   
    if direction == "North":
        print("You went North")
    
    elif direction == "South":
        print("You went South")
    
    elif direction == "East":
        print("You went East")
    
    elif direction == "West":
        print("You went West")

    else:
        print("Sorry,not recognised")        














main()
