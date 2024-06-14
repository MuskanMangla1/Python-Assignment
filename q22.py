def q22(list1):
    max = list1[0]
    min = list1[0]
    for item in list1 :
        if(item < min):
            min = item
        else:
            max = item
    
    print("max value = {}\nmin value = {}".format(max,min))

c = int(input("enter the number of elements in list :"))
l = []
for i in range (0,c):
    l.append(str(input(f"list[{i}] = ")))
q22(l)