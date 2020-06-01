def sum(list,size,sum):
   sumlist = []
   if size == 1:
      for x in list:
           sumlist.append(sum + x)
       return sumlist
  L2 = list(list)
  for x in list:
      L2.remove(x)
      sumlist.extend(sum(L2,size-1,sum + x))
 return sumlist
 
 def summation(list,size):
     sumlist = list(list)
     for i in range (2, size + 1):
         sumlist.extend(sum(list, i, 0))
     number = 1
     while true:
        if number not in sumlist:
            print("the least integer which is not present in the list and also cannot be represented as the summation of list:")
            break
        number += 1
        
        size = int(input("enter the no of elements you want to add in the list:"))
        list = []
        print("enter the elements in list one by one:")
        for i in range(size):
          list.append(int(input()))
        summation(list, size)
