def GetAbhishekName():
    return "Abhishek yelmamdi"

while True:
    Argument= input()
    
    if Argument == "Abhishek":
        print(GetAbhishekName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
