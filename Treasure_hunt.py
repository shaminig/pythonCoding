print("Welcome to the TREASURE HUNT")
start=input('you know to swim "yes" or "no"//n').lower()
if(start=='yes'):
    print("you reached the shore")
else:
    print("your game is over/n.without knowing to swim you cannot reach the treasure/n")
find_key=input('you have the option of choosing between 2 boxes."one" is box of crabs,"two" is box of prawns/n')
if(find_key=='one'):
    print("you found the key")
else:
    print("you lost the game")
door=input("you could choose the color of door in which the treasure is present/n")
if(door=='blue'and door=='red'):
    print("lost the game")
else:
    print("found the treasure.you won the game/n")
