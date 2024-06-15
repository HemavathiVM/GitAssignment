def GetmyName():
    return "chetan donawadi"

while True:
    Argument= input()
    
    if Argument == "chetan":
        print(GetmyName())
    
    elif Argument == "exit":
        break
    
    else:
        print("Invalid argument")
