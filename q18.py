def q18():
    str1 = str(input("enter 1st string : "))
    str2 = str(input("enter 2nd string : "))

    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    if(len(str1) != len(str2)):
        return False 

    freq1 = {}
    freq2 = {}

    for char in str1 :
        freq1[char] = freq1.get(char,0)+1

    for char in str2 :
        freq2[char] = freq2.get(char,0)+1

    return freq1 == freq2 

q18()