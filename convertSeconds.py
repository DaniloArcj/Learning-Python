while True :
    seconds = input("Type how many seconds: ")
    if seconds == "exit" :
        break
    else :
        day = ((int(seconds)//60)//60)//24
        hrs = ((int(seconds)//60)//60)%24
        min = (int(seconds)//60)%60
        sec = int(seconds)%60
    
        print(seconds, "sec = ", day, "day", hrs, "hrs", min, "min", sec, "sec", "\n")