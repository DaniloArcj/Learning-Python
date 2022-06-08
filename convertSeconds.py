while True :
    seconds = input("Type how many seconds: ")
    if seconds == "exit" :
        break
    else :
        day = ((int(seconds)//60)//60)//24
        hrs = ((int(seconds)//60)//60)%24
        min = (int(seconds)//60)%60
        sec = int(seconds)%60
    
        if day == 0: 
            if hrs == 0 :
                if min == 0 :
                    if sec == 0 :
                        print("You typed 0 seconds", "\n")
                    else :
                        print(seconds, "sec = ", sec, "sec", "\n")
                else :
                    if sec == 0 :
                        print(seconds, "sec = ", min, "min", "\n")
                    else :
                        print(seconds, "sec = ", min, "min", sec, "sec", "\n")
            else :
                if min == 0 :
                    if sec == 0 :
                        print(seconds, "sec = ", hrs, "hrs", "\n")
                    else :
                        print(seconds, "sec = ", hrs, "hrs", sec, "sec", "\n")
                else :
                    if sec == 0 :
                        print(seconds, "sec = ", hrs, "hrs", min, "min", "\n")
                    else :
                        print(seconds, "sec = ", hrs, "hrs", min, "min", sec, "sec", "\n")
        else :
            if hrs == 0 :
                if min == 0 :
                    if sec == 0 :
                        print(seconds, "sec = ", day, "day", "\n")
                    else :
                        print(seconds, "sec = ", day, "day", sec, "sec", "\n")
                else :
                    if sec == 0 :
                        print(seconds, "sec = ", day, "day", min, "min", "\n")
                    else :
                        print(seconds, "sec = ", day, "day", min, "min", sec, "sec", "\n")
            else :
                if min == 0 :
                   if sec == 0 :
                        print(seconds, "sec = ", day, "day", hrs, "hrs", "\n")
                   else :
                        print(seconds, "sec = ", day, "day", hrs, "hrs", sec, "sec", "\n")
                else :
                    if sec == 0 :
                        print(seconds, "sec = ", day, "day", hrs, "hrs", min, "min", "\n")
                    else :
                        print(seconds, "sec = ", day, "day", hrs, "hrs", min, "min", sec, "sec", "\n")

