def GetAdityaName():
    return "Aditya N M"

def GetAbhimanyuName():
    return "ABHIMANYU SINGH"

while True:
    Argument= input()
    
    if Argument == "Aditya":
        print(GetAdityaName())

    if Argument == "ABHIMANYU":
        print(GetAbhimanyuName())
    
    elif Argument == "exit":
        break

    
    else:
        print("Invalid argument")
