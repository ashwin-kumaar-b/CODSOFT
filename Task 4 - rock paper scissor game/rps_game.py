import random
import string
ap=hp=0
def botans():
    ans=random.choice(["rock","paper","scissor"])
    return ans

def game(ai,human):
    global ap,hp
    if ai==human:
        print("tie")
    elif ai=="rock" and human=="scissor":
        print("bot wins!")
        ap+=1
    elif ai=="scissor" and human=="rock":
        print("you win")
        hp+=1
    elif ai=="rock" and human=="paper":
        print("you win!")
        hp+=1
    elif ai=="paper" and human=="rock":
        print("bot wins!")
        ap+=1
    elif ai=="scissor" and human=="paper":
        print("bot wins!")
        ap+=1
    elif ai=="paper" and human=="scissor":
        print("you win!")
        hp+=1
def rps():
    ai=botans()
    human=input("enter your choice(rock/paper/scissor):")
    human=human.lower()           
    a=["rock","paper","scissor"]
    if(human in a):
        print("bot chose",ai)
        game(ai,human)
    else:
        print("enter a valid choice")
    print("\n\n")
    choices()
def main():
    choice=input("would you like to play a game?(yes/no):")
    if choice.lower()=="yes":
        rps()
    elif choice.lower()=="no":
        print("exiting..")
    else:
        print("invalid \n")
def choices():
    while True:
        print("1.play again\n2.display scores\n3.end game")
        try:
             choice=int(input("enter your choice(1/2/3):"))
        except ValueError as e:
             print("enter only numbers\n")
             continue
        
    
        
        if choice==1:
            rps()
            break
        elif choice==2:
            print("\n")
            print("bot score:",ap)
            print("your score:",hp)
            print("\n")
            
        elif choice==3:
            print("exiting..")
            break
        else:
            print("invalid choice")


main()
    


    


