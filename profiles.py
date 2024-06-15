def GetSrinidhiName():
    return "Srinidhi S Nayaka"

while True:
    Argument= input()
    
    if Argument == "Srinidhi":
        print(GetSrinidhiName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
