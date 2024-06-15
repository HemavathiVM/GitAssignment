def GetAdityaName():
    return "Aditya N M"
def GetSuprabathName():
    return "Surpabath reddy"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())

    elif Argument =="Surpabath":
        print(GetSuprabathName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
