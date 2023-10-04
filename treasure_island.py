print("Welcome to Treasure Island")
choose_dir=input("Choose the direction LEFT OR RIGHT   ")
if(choose_dir=='LEFT'):
    want_swim=input("want to swim y orn n   ")
    if(want_swim=='Y'):
        print("your game is over (hunted by trouts)")
    else:
        print("wait here to choose the right door to hunt the treasure")
        choose_door=input("choose between red,blue and yellow")
        if choose_door=='BLUE':
            print("hunted by beast.game is over")
        elif choose_door=='RED':
            print("fire!!!!game is over")
        else:
            print("you win!!!!!chosen the right door YELLOW")
else:
    print("your game is over CHOSEN RIGHT DIRECTION")



