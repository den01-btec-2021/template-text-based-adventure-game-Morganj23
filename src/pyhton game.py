def main():
    print("Welcome to my game")

    player_name=input("what is your name? ")
    print("Hi " + player_name)

    backpack = [] #initialsise empty list for backpack
    lives = 3
    print(f"You have {lives} lives remaining, make them count!")
    print("You are located in an abandoned laboratory and you must find away to get out" )
    print("To successfully leave the building you must enter 4 other rooms in which you will enntouer puzzles which will be rquired towards the end of the game" )
    

    print("You notice a door ahead of you which looks to be pried open")

    print("To move towards the enter North")
    
    
    while True:
        direction =input("Which direction do you want to go? ")
        
        if direction == "North":
            print("You went North")
            puzzle_answer_North = input("What is 2+2? ")
            if puzzle_answer_North == "4":
                print("Correct")
                backpack.append("Key 1")

            else:
                print("Incorrect")
                lives -= 1
                print(f"You have {lives} lives remaining ")
        
        
        
        
        
        
        
        elif direction == "South":
            print("You went South")
        
        elif direction == "East":
            print("You went East")
        
        elif direction == "West":
            print("You went West")

        else:
            print("Sorry,not recognised") 


        #if backpack is full, open door, win game  
        if ("Key 1"in backpack) and ("Key 2"in backpack) and ("Key 3"in backpack) and ("Key 4"in backpack):
            print("Vents open!, you got out")
        
        #when lives reach 0, game ends
        if lives == 0:
            print("You perished")  
            exit()   














main()
