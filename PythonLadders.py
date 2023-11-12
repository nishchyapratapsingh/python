#We are trying to make a basic snake and ladders game
from time import sleep #for pauses
import random #for tosses and dice rolls
def snakeandladders(score):
    ### Ladders
    if score == 8:
      print("You went up a ladder! +15! ")
      return score+15
    if score == 50:
      score=80
      print("You went up a ladder! +30! ")
    if score == 2:
      score=52
      print("You went up a ladder! +50 ")
    if score == 12:
      score=92
      print("You went up a ladder! +80 ")
    ### Snakes
    if score == 35:
      score=13
      print("You got bitten by a snake! -22 ")
    if score == 70:
      score=40
      print("You got bitten by a snake! -30 ")
    if score == 99:
      score=29
      print("You got bitten by a snake! -70 ")
    return score

    ### Snakes and Ladders done
print("Welcome to Python Ladders...")
sleep(0.2)
print("*************************************")
sleep(0.2)
print("a game by Nishchya and Chaitanya")
sleep(0.2)
print("*************************************")
sleep(0.5)
input("Press enter to continue... ")
board_size = int(input("Enter the size of the board between 20 and 1000: "))
if board_size < 20 or board_size >1000:
                 boardsize = 100
                 print("Default size (100) will be used!")
num_players = int(input("Enter the number of players: ")) #Lets try to make it a multiplayer game
players = []
for i in range(num_players):
    name = input("Enter the name of player {}: ".format(i+1)) #i+1 because i has initial value 0
    players.append({"name": name, "score": 0}) # We create a list of dictionaries... Each dictionary represent one player
    
#Maybe in future we may add a loop so that there can be n number of players but as of now lets stick to 2 ##In progress
#score1,score2 = 0,0 #initialise the scores # One can also initialize them with different values to test the code without playing the whole game
input("Press enter for toss ")
sleep(0.5)
toss_winner = random.choice(players)
print("{} won the toss!\n{} goes first ".format(toss_winner['name'], toss_winner['name']))
players.sort(key = lambda x: x!= toss_winner) #Put the toss winner in first position as it returns false thus having low place in list
while all(player["score"] < board_size for player in players): #when all scores are less than 100
 for player in players: #iterates through all players
    sleep(0.2)
    print("*****************************************")
    sleep(0.3)
    print("Turn: {}\nScore: {}".format(player['name'],player['score']))
    input("Press enter to play")
    dice = random.randint(1,6)
    player['score'] += dice
    player['score'] = snakeandladders(player['score'])
    if player['score']>board_size:
      player['score'] -= dice   #in case the score exceeds 100
    sleep(0.5)
    print("You got {}\nYour score is {}".format(dice,player['score']))
    sleep(0.6)
    print("*****************************************")
print("*****************************************")
print("*****************************************")
print("*****************************************")
sleep(0.6)
for player in players:
 if player['score']==board_size:
  print("{} is the winner!!".format(player['name']))
print("*****************************************")
print("*****************************************")
print("*****************************************")
