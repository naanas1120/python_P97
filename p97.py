import random 

randomNo=random.randint(1,9)
chances=0

while chances < 5:
    guess=input("guess the number:")

    chances+=1
    if guess == randomNo:
      print("congratulations you won")
      break
    else:
        print("try again")  
