def GetAdityaName():
    return "Aditya N M"

def GetAbhishek_S():
    return "Abhishek_S"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())

    elif Argument == "AbhishekS":
        print(GetAbhishek_S())

    elif Argument == "exit":
        break 

    else:
        print("Invalid argument")
