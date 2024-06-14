def q26():
    string = str(input("enter the string : "))
    prefix = str(input("enter the prefix : "))
    suffix = str(input("enter the suffix : "))
    if string.startswith(prefix) :
        print(f"The string starts with the prefix '{prefix}'.")
        if string.endswith(suffix) :
            print(f"The string ends with the suffix '{suffix}'.")
        else :
            print(f"The string doesn't ends with the suffix '{suffix}'.")
    elif string.endswith(suffix) :
            print(f"The string doesn't starts with the prefix '{prefix}'.")
            print(f"The string ends with the suffix '{suffix}'.")
    else:
        print("The string does not start with the given prefix or end with the given suffix.")


q26()