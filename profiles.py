def GetAdityaName():
    return "Aditya N M"

def GetOmkarName():
    return "Omkar M H"

while True:
    Argument= input()
    
    if Argument == "Omkar":
        print(GetOmkarName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
