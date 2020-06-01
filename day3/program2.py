def permutation(list, string =""):
    set = set(list)
    stringlist = []
    if len(set) == 1:
      string += "".join(list)
      return list([string])
 for x in set:
     list1 = list(list)
     S = string + x
     list1.remove(x)
     stringlist.extend(permutation(list1,S))
 return stringlist
 
 string = input("enter a string:")
 list = permutation(list(string))
 print("all the permutation of the given string is ;" +  ", ".join(list))
   
