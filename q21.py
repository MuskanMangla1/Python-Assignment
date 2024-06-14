def q21(list1 , element):
    count = 0 
    for item in list1:
        if item == element:
            count += 1
    print(count)

c = int(input("enter the number of elements in list :"))
l = []
for i in range (0,c):
    l.append(str(input(f"list[{i}] = ")))
element = str(input("enter the element : "))
q21(l,element)