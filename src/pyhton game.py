from ast import Return, While
from pdb import Restart


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
            room_number = "1"
            puzzle = "6*6?"
            puzzle_answer = "36"
            screwdriver_colour ="Blue screwdriver"
            in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)







        elif direction == "South":
            print("You went into Room2")
            


        
        elif direction == "East":
            print("You went into Room3")
        
        elif direction == "West":
            print("You went Room4")

        else:
            print("Sorry,not recognised") 


        #if backpack is full, open door, win game  
        if ("Blue screwdriver"in backpack) and ("Red screwdriver"in backpack) and ("Black screwdriver"in backpack) and ("Yellow screwdriver"in backpack):
            print("Vents open!, you got out")
        
         






    





def in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour):
    print(f"You went into {room_number} Room.")
    #flag that the puzzle is not solved by default
    puzzle_solved=False
     #while we still have lives and the puzzle is not solved, loop round
    while (puzzle_solved == False and lives > 0):
        puzzle_answer_North = input(puzzle)
        if puzzle_answer_North == puzzle_answer:
            print(f"Correct. screwdriver {screwdriver_colour} collected.")
            backpack.append(f"screwdriver {screwdriver_colour}")
             #puzzle is solved set flag to true
            puzzle_solved=True
        else:
            print(f"Incorrect")
            lives -= 1
            print(f"You have {lives} lives remaining. ")

           #when lives reach 0, game ends
        if lives == 0:
            print("You perished") 
            exit()  

if __name__=="__main__":
    main()
