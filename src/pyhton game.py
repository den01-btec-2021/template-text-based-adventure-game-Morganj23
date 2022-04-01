from ast import Return, While
from pdb import Restart
import time

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
            screwdriver_colour ="Blue"
            in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)
              




        elif direction == "South":
            room_number = "2"
            puzzle = "What language do they speak in Brazil?"
            puzzle_answer = "Portuguese"
            screwdriver_colour ="Red"
            in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)
             
            


        
        elif direction == "East":
            room_number = "3"
            puzzle = "Which former president made an appearance in Home Alone 2?"
            puzzle_answer = "Donald Trump"
            screwdriver_colour ="Black"
            in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)
              
        
       
    
    
        elif direction == "West":
            room_number = "4"
            puzzle = "What city did the Americans use an atomic bomb on in 1945?"
            puzzle_answer = "Hiroshima"
            screwdriver_colour ="Yellow"
            in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)
            

        else:
            print("Sorry,not recognised") 


        #if backpack is full, open door, win game  
        if ("Blue screwdriver"in backpack) and ("Red screwdriver"in backpack) and ("Black screwdriver"in backpack) and ("Yellow screwdriver"in backpack):
            print("Vents open!, you got out")
             
        
         






    

def in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour):
    print(f"You went into {room_number} Room. Timer has began. You have 5 seconds to solve this.")
    #start the timer
    time_elapsed = time.time()
    #if 5 seconds has passed,lose life
    

    #flag that the puzzle is not solved by default
    puzzle_solved=False
     #while we still have lives and the puzzle is not solved, loop round
    while (puzzle_solved == False and lives > 0):
        puzzle_answer_North = input(puzzle)
        if puzzle_answer_North == puzzle_answer:
            print(f"Correct. screwdriver {screwdriver_colour} collected.")
            #checking if they have already collected this screwdriver
            if f"screwdriver {screwdriver_colour}" not in backpack:
                backpack.append(f"{screwdriver_colour} screwdriver")
            else:
                print("you already have this screwdriver")
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
    return lives

#def addition(a,b):
    return a + b

#def test_addition():
    assert addition(3,5) == 8
    assert addition(-1,0) == -1
    assert addition(-1,1) == 0


#def test_in_room():

    backpack = []
    lives = 3
    room_number = "1"
    puzzle = "6*6"
    puzzle_answer = "36"
    screwdriver_colour = "Blue"

   #check incorrect
   #  assert in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour) == 2 # lives -1

#check correct?
    #assert in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour) == 3 # lives =
    #assert f"{screwdriver_colour} screwdriver" in backpack #check that the key is in backpack

   # in_room(backpack,lives,room_number,puzzle,puzzle_answer,screwdriver_colour)
    #assert backpack != ["Blue screwdriver","Blue screwdriver"]

            

if __name__=="__main__":
    main()
    #value = addition (3,2)
    #print(value)
    #test_addition
    #test_in_room()
