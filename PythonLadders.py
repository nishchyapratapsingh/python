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
    ### !!The function is not increasing the score!!
print("Welcome to Python Ladders...")
sleep(0.2)
print("*************************************")
sleep(0.2)
print("a game by Nishchya and Chaitanya")
sleep(0.2)
print("*************************************")
sleep(0.5)
input("Press enter to continue... ")
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
#Maybe in future we may add a loop so that there can be n number of players but as of now lets stick to 2
score1,score2 = 0,0 #initialise the scores #### One can also initialize them with different values to test the code without playing the whole game
input("Press enter for toss ")
sleep(0.5)

toss = random.randint(1,2) #toss
if toss == 1:
  print("{} won the toss...".format(player1))
  p1 = player1
else:
  print("{} won the toss...".format(player2))
  p1 = player2
  temp1 = score1
  score1 = score2
  score2 = temp1  #swapping the scores
if p1==player1:  #specifying the player with first move (There can be better ways but currently I am aware of these only)
  p2 = player2
else:
  p2 = player1  #adjusting the first turn with the toss result
print("{} goes first".format(p1))
while(score1!=n and score2!=100):
    sleep(0.2)
    print("*****************************************")
    sleep(0.3)
    print("Turn: {}\nScore: {}".format(p1,score1))
    input("Press enter to play")
    dice = random.randint(1,6)
    score1 += dice
    score1 = snakeandladders(score1)
    if score1>100:
      score1 -= dice   #in case the score exceeds 100
    sleep(0.5)
    print("You got {}\nYour score is {}".format(dice,score1))
    sleep(0.6)
    print("*****************************************")
    sleep(0.3)
    print("Turn: {}\nScore: {}".format(p2,score2))
    sleep(0.5)
    input("Press enter to play")
    dice = random.randint(1,6)
    score2 += dice
    score2 = snakeandladders(score2)
    if score2>100:
      score2 -= dice
    sleep(0.5)
    print("You got {}\nYour score is {}".format(dice,score2))  #basics are done. Now lets add some snakes and ladders ##Done Nov 10,2023
print("*****************************************")
print("*****************************************")
print("*****************************************")
sleep(0.6)
if score1==100:
  print("{} is the winner!!".format(p1))
if score2==100:
  print("{} is the winner!!".format(p2))
print("*****************************************")
print("*****************************************")
print("*****************************************")
