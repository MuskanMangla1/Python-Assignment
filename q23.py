def q23():
    choice = str(input("enter\nc for celsius\nf for fahrenheit\n:"))
    if choice == 'c' or choice == 'C' :
        cel_val = float(input("enter the celsius value : "))
        print("{} C = {} F".format(cel_val,(cel_val * 9/5) + 32))
    elif choice == 'f' or choice == 'F' :
        fah_val = int(input("enter the celsius value : "))
        print("{} F = {} C".format(fah_val,(5*fah_val/9)+32))
    else :
        print("Invalid input")

q23()