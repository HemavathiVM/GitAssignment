def GetVidhaanName():
    return "Vidhaan Viswas"

while True:
    Argument= input()
    
    if Argument == "Vidhaan":
        print(GetVidhaanName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
