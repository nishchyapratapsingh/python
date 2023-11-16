#Snake and Ladders simulation
#PYTHON LADDERS
#Nishchya Pratap Singh
#Chaitanya Chaudhary
#Dev Yadav
from time import sleep #for pauses
import random #for tosses and dice rolls
def dicefn(player):
    dice = random.randint(1, 6) #rolling the dice
    player['score'] += dice
    while dice == 6:
        if (player['score']+6)<100:  #makes sure that player doesn't get the extra chance if score exceeds or equals 100
            input("You got 6!\nOne more chance!\nPress Enter to play ")
            dice = random.randint(1, 6)
            player['score'] += dice
        elif (player['score']+6)==100:
            print("Can not go to 100 with 6! ")
        else:
            break
            
    return dice, player['score']
def snakeandladders(score): #adding snakes and ladders
    if score == 8:
      print("You went up a ladder! +15! ")
      return score+15
    if score == 50:
      score=80
      print("You went up a ladder! +30! ")
    if score == 4:
        score=90
        print("You went up a ladder! +86")
    if score == 2:
      score=52
      print("You went up a ladder! +50 ")
    if score == 12:
      score=92
      print("You went up a ladder! +80 ")
    if score == 35:
      score=13
      print("You got bitten by a snake! -22 ")
    if score == 70:
      score=40
      print("You got bitten by a snake! -30 ")
    if score == 90:
      score=29
      print("You got bitten by a snake! -70 ")
    return score
print("Welcome to Python Ladders...") #First message
sleep(0.2)
print("*************************************")
sleep(0.2)
print("a python project by Nishchya, Chaitanya and Dev")
sleep(0.2)
print("*************************************")
sleep(0.5)
input("Press enter to continue... ")
num_players = int(input("Enter the number of players: ")) #multiplayer
players = [] #create a list to store players and scores
for i in range(num_players):
    name = input("Enter the name of player {}: ".format(i+1)) #i+1 because i has initial value 0
    players.append({"name": name, "score": 0}) # We create a list of dictionaries... Each dictionary represent one player
input("Press enter for toss ")
sleep(0.2)
toss_winner = random.choice(players) #select a random player to play first
print("{} won the toss!\n{} goes first ".format(toss_winner['name'], toss_winner['name']))
players.sort(key = lambda x: x!= toss_winner) #This puts the toss winner in first position as tosswinner returns false thus having low place in list
win = 0 
while win != 1: 
 for player in players: #iterates through all players
    sleep(0.1)
    print("*****************************************")
    sleep(0.1)
    print("Turn: {}\nScore: {}".format(player['name'],player['score']))
    input("Press enter to play")
    dice,player['score'] = dicefn(player) #Take the value of dice from dicefn
    player['score'] = snakeandladders(player['score']) #optimise score according to the snakeandladders function
    if player['score']>100:
      player['score'] -= dice   #in case the score exceeds 100
    sleep(0.2)
    print("You got {}\nYour score is {}".format(dice,player['score']))
    sleep(0.2)
    print("*****************************************")
    if player['score']==100: #Declare the winner
        print("*****************************************")
        print("*****************************************")
        print("{} is the winner!!".format(player['name']))
        print("*****************************************")
        print("*****************************************")
        win = 1 #we use this variable to terminate the while loop on the end of the game
        break
