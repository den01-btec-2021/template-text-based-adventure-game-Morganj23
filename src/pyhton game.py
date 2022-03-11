from ast import Return, While


def main():
    print("Welcome to my game")

    player_name=input("what is your name? ")
    print("Hi " + player_name)

    backpack = [] #initialsise empty list for backpack
    lives = 3
    print(f"You have {lives} lives remaining, make them count!")
    print("You are located in an abandoned laboratory and you must find away to get out" )
    print("To successfully leave the building you must enter 4 other rooms in which you will encounter puzzles which will be rquired towards the end of the game" )
    
    print("You notice a door ahead of you which looks to be pried open")

    direction =input("To contiunue North press Enter")
    
    print("you enter a long dark corridor,you notice there are 4 doors numbered 1,2,3 and 4")
    print("Door1 = North, Door2 = South, Door3 = East, Door4 = West")

    
    while True:
        direction =input("Which direction do you want to go? ")
        
        if direction == "North":
            print("You went North")
            puzzle_answer_North = input("6*6? ")
            if puzzle_answer_North == "36":
                print("Correct")
                backpack.append("Blue screwdriver")

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
        if ("Blue screwdriver"in backpack) and ("Red screwdriver"in backpack) and ("Black screwdriver"in backpack) and ("Yellow screwdriver"in backpack):
            print("Vents open!, you got out")
        
        #when lives reach 0, game ends
        if lives == 0:
            print("You perished")  
            exit()   














main()
