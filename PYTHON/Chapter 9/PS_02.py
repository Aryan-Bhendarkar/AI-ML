import random 

def game():
    print("You are playing the game..")
    score = random.randint(1,62) 
    # Fetch the random score 
    with open("Chapter 9/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ''):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score : {score}")
    # Update the hignscore
    if(score > hiscore):
        with open("Chapter 9\hiscore.txt" , "w") as f :
            f.write(str(score))

    return score

game()