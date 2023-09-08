import random
name=input("\t\t\t\tenter your name:")
def computer_choice():
    number = random.randint(1, 100)
    b=number
    attemp=1
#def guess_a_number():
    print("\t\t\tplease guess a number between 1 to 100")
    a=int(input("\t\t\t\tguess the number:"))
    while b!=a:
        attemp+=1
        if a>100:
            print("\t\t\tplease read the sentense and try again")
            break
        elif b>a:
            print("\t\t\tplease enter a large number of",a)
            
        elif a>b:
            print("\t\t\tplease enter a lower number of",a)
        
        a=int(input("\t\t\t\tguess the number:"))
        continue
    print("\t\t\t\tcorrect number")
    print("\t\twow",name,"congratulation you guess the number in ",attemp,"attemps")

if __name__=="__main__":
    computer_choice()
     