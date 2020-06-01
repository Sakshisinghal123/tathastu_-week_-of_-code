size1 = int(input("enter the no of elements you want to enter in the list 1:"))
print("enter the elements in list1 one by one")
list1 = []
for i in range(size1):
   list1.append(input())
size2 = int(input("enter the number of elements you want to enter in the list 2:")
print("enter the elements in list2 one by one")
list2 = []
for i in range(size2):
   list2.append(input())
intersectionList = list(set(list1).intersection(set(list2)))
print("the intersection of list 1 and list 2 is :", ", ".join(intersectionList))
