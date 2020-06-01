def duplicate(list):
  duplicatelist = []
  for x in list:
      if x not in duplicatelist:
          duplicateList.append(x)
   return duplicateList
   
   size = int(input("enter the no of elements you want to add in list:"))
   print("enter the elements in list one by one")
   List = []
   for i in range(size):
       List.append(input())
   print("list after removing the duplicates is :", duplicate(list))
   
   
   
      
