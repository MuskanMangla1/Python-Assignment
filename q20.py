def q20():
    list1 = []
    sum = 0
    i = int(input("enter the number of elements you want in list : "))
    for x in range(0,i):
        val = int(input("list[{}] = ".format(x)))
        list1.append(val)
    for x in list1 :
        sum += x
    
    print("sum is : ",sum)

q20()