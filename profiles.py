def GetAdityaName():
    return "Aditya N M"

def GetRohitName():
    return "Rohit y" 

def GetCharanName():
    return "Sri Charan"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())
    
    if Argument == "Charan":
        print(GetCharanName())
    
    elif Argument == "Rohit":
        print(GetRohitName())

    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
