n = int(input("enter the value of N:"))
for i in range(n):
   print("* " * (n-i) + "    " * i + " *" * (n-1))
   for i in range(2,n+1)
    print("* " * i + "    " * (n-i) + " *" * i)
