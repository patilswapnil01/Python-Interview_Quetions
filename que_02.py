# Python program to reverse a number
from audioop import reverse


x = int(input("Enter the number here to reverse it : "))
print("Before the reveresing-->",x)

reverse = 0
while x!= 0:
    reverse = reverse*10 + x%10
    x= (x//10)
print("After revrese the number is : ",reverse)