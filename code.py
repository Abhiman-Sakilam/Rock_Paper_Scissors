import random    
i = 0
j = 0
loop = 0                           
for loop in range(0,11):  
    
        options = ["Rock","Paper","Scissors"]
        
        random_choice= random.randrange(0,len(options))
        
        System =options[random_choice]
    
    
        User = str(input("please give your input : ").capitalize())
    
        if (User=="Rock"):
            if System == "Rock":
                print("System's choice :",System)
                print("Tie")

            elif System =="Scissors":
                print("System's choice :",System)
                print("You won")
                i=i+1

            elif System == "Paper":
                print("System's choice :",System)
                print("You lost")
                j = j+1

        if (User=="Paper"):
            if System == "Rock":
                print("System's choice :",System)
                print("You won")
                i = i+1

            elif System =="Scissors":
                print("System's choice :",System)
                print("You lost")
                j = j+1

            elif System=="Paper":
                print("System's choice :",System)
                print("Tie")
                 


        if (User=="Scissors"):
            
            if System == "Rock":
                print("System's choice :",System)
                print("You lost")
                j= j+1

            elif System =="Scissors":
                print("System's choice :",System)
                print("Tie")


            elif System == "Paper":
                print("System's choice :",System)
                print("You won")
                i= i+1
       
        ++loop  

points = {
    "wins" : i,
    "loses" : j
}
points.update()
print("Your Score: ",points)
