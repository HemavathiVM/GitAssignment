
def Abhishek_S():
    return "Abhishek_S"

def GetVidhaanName():
    return "Vidhaan Viswas"

def GetCharanName():
    return "Sri Charan"


while True:
    Argument= input()
    

    if Argument == "Abhishek":
        print(GetAdityaName())

    if Argument == "Vidhaan":
        print(GetVidhaanName())
    
    if Argument == "Charan":
        print(GetCharanName())

    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
