def is prime(N):
a=2
k = N // 2
while k>=a:
  if N%a==0:
     return false
   a+=1
   k = N // a
   return true
   
 def is palindrome(n):
   N = str(n)
   L =len(N)
   for i in range (L // 2):
     if N(i) != N[L-1-i]:
       return false
   return true
   
 def is odd(n):
    if n % 2 ==0:
       return false
     return true
     
  def is atmstrong(num):
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit**3
       temp //= 10
    if num == sum:
       return true
     return false
     
   def check():
   number = int(input("enter the number:"))
   if(is prime(number)):
       print(number,"is a prime number")
   if(is odd(number)):
        print(number,"is an odd number")
   else:
       print(number,"is an even number")
   if(is palindrome(number)):
        print(number,"is a palindrome nuumber")
   if(is armstrong(number)):
        print(number,"is an armstrong number")
        
   check()
     
   
     
