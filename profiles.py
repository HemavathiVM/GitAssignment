def GetSanketName():
    return "Sanket Muttur"

while True:
    Argument= input()
    
    if Argument == "Sanket":
        print(GetSanketName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
