def GetAdityaName():
    return "Aditya N M"
def GetBhoomiName():
    return "Bhoomika R P"
def GetHemaName():
    return "Hemavathi V M"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())
    if Argument == "Bhoomika":
        print(GetBhoomiName())
    if Argument == "Hemavathi":
        print(GetHemaName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
