while True :
    seconds = input("Type how many seconds: ")
    if seconds == "exit" :
        break

    day = ((int(seconds)//60)//60)//24
    hrs = ((int(seconds)//60)//60)%24
    min = (int(seconds)//60)%60
    sec = int(seconds)%60
       
    if (day == 0) and (hrs == 0) and (min == 0) and (sec == 0):
        print("You typed 0 seconds", "\n")

    if (day == 0) and (hrs == 0) and (min == 0) and (sec != 0):
        print(seconds, "sec = ", sec, "sec", "\n")

    if (day == 0) and (hrs == 0) and (min != 0) and (sec == 0):
        print(seconds, "sec = ", min, "min", "\n")

    if (day == 0) and (hrs == 0) and (min != 0) and (sec != 0):            
        print(seconds, "sec = ", min, "min", sec, "sec", "\n")

    if (day == 0) and (hrs != 0) and (min == 0) and (sec == 0):
        print(seconds, "sec = ", hrs, "hrs", "\n")

    if (day == 0) and (hrs != 0) and (min == 0) and (sec != 0):
        print(seconds, "sec = ", hrs, "hrs", sec, "sec", "\n")

    if (day == 0) and (hrs != 0) and (min != 0) and (sec == 0):
        print(seconds, "sec = ", hrs, "hrs", min, "min", "\n")

    if (day == 0) and (hrs != 0) and (min != 0) and (sec != 0):
        print(seconds, "sec = ", hrs, "hrs", min, "min", sec, "sec", "\n")

    if (day != 0) and (hrs == 0) and (min == 0) and (sec == 0):
        print(seconds, "sec = ", day, "day", "\n")

    if (day != 0) and (hrs == 0) and (min == 0) and (sec != 0):
        print(seconds, "sec = ", day, "day", sec, "sec", "\n")

    if (day != 0) and (hrs == 0) and (min != 0) and (sec == 0):
        print(seconds, "sec = ", day, "day", min, "min", "\n")

    if (day != 0) and (hrs == 0) and (min != 0) and (sec != 0):
        print(seconds, "sec = ", day, "day", min, "min", sec, "sec", "\n")

    if (day != 0) and (hrs != 0) and (min == 0) and (sec == 0):
        print(seconds, "sec = ", day, "day", hrs, "hrs", "\n")

    if (day != 0) and (hrs != 0) and (min == 0) and (sec != 0):
        print(seconds, "sec = ", day, "day", hrs, "hrs", sec, "sec", "\n")

    if (day != 0) and (hrs != 0) and (min != 0) and (sec == 0):
        print(seconds, "sec = ", day, "day", hrs, "hrs", min, "min", "\n")

    if (day != 0) and (hrs != 0) and (min != 0) and (sec != 0):
        print(seconds, "sec = ", day, "day", hrs, "hrs", min, "min", sec, "sec", "\n")