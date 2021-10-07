import random #to generate computer choices
def game(comp,you):
    if comp=="snake" and you=="gun":
        return print(" --------Hurray! Player wins--------")
    elif comp=="water" and you=="snake":
        return print(" --------Hurray! Player wins--------")
    elif comp=="gun" and you=="water":
        return print(" --------Hurray! Player wins--------")
    elif comp==you:
        return print("---------Match Ties----------")
    else:
        return print("-----------Computer wins------------")
comp=random.randint(1,3)
you=input("Player Choose from\tsnake\twater\tgun\n") #user input
if you==("snake" or "water" or "gun"): #correct input  
    if comp==1:
        comp="snake"
    elif comp==2:
        comp="water"
    elif comp==3:
        comp="gun"
    print(f"Computer choice----------{comp}\n")
    game(comp,you)
else:
    print("----------Oops!,Wrong input, please restart game------------------")