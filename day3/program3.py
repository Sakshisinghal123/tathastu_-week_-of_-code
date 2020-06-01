def duplicate(string):
  duplicateString = ""
  for x in string:
      if x not in duplicatesString:
          duplicatesString += x
   return duplicatesString
   
   string = input("enter the string:")
   print("string after removing the duplicates is :", duplicate(string))
   
      
