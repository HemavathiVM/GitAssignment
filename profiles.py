def GetAdityaName():
    return "Aditya N M"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")