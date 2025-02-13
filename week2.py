
while(True):
    name=input("What is your name? ")
    if name=="":
        print("please enter something ")
        continue
    
    print(f' Hello, {name} ,nice to meet you!')

    #writing the code without variables
    #print(" Hello, "+input("What is your name? ") +",nice to meet you!'")
    # Write a version of the program that displays different greetings for different people.
    if name=="Heba":
        print(f' Welcome , {name} ,nice to meet you!')
    elif name=="Emad":
        print(f' Hi , {name} ,nice to meet you!')
    else:
        print(f' Hello Hello , {name} , welcome to our community!')
        
    #Counting the Number of Characters
    name_num=input("What is the input string? ")
    
    if name_num=="":
        print("please enter something! ")
        continue
    print(f'{name} has {len(name_num)} characters.')
    break