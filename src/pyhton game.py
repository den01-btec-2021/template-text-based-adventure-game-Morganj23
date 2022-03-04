from itertools import count


def main():
    print("Welcome to my game")

    player_name=input("what is your name? ")
    print("Hi " + player_name)

    lives = 3
    print(f"You have {lives} lives remaining")

    print("")

    print("you can move North,South,East,West")
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