def q24():
    num1 = float(input("enter number1 : "))
    num2 = float(input("enter number2 : "))
    while True :
        choice = str(input("enter\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\nq for quit\n"))
        if choice == '+' :
            print(f"The result is: {num1 + num2}")
        elif choice == '-' :
            print(f"The result is: {num1 - num2}")
        elif choice == '*' :
            print(f"The result is: {num1 * num2}")
        elif choice == '/' :
            print(f"The result is: {num1 / num2}")
        else :
            print("quitting")
            break

q24()