def q14():
    lines = []
    print("Enter lines of text. To stop, just press Enter on an empty line:")

    while True :
        line = input()
        if line == "" :
            break 
        lines.append(line)
    
    print("You Entered")
    for line in lines :
        print(line)

q14()