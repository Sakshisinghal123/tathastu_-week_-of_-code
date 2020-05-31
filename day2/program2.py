N = int(input("enter the value of N:")
a = 0
b = 1
print("the fibonacci series upto", "th number is following:")
for i in range(N):
   print(a, end = " ")
   c = a + b
   a = b
   b = c
   
