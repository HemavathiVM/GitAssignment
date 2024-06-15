
def GetCharanName():
    return "Sri Charan"

def GetPuneethName():
    return "Puneeth M S"

while True:
    Argument= input()

    
    if Argument == "Charan":
        print(GetCharanName())

    if Argument == "Puneeth":
        print(GetPuneethName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
