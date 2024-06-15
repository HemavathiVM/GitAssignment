def GetAdityaName():
    return "Aditya N M"

def GetCharanName():
    return "Sri Charan"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())
    
    if Argument == "Charan":
        print(GetCharanName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
