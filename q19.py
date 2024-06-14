import string
def q19(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to remove all punctuation
    return input_string.translate(translator)


input_string = str(input("enter a string : "))
cleaned_string = q19(input_string)
print("Original string:", input_string)
print("Cleaned string:", cleaned_string)

