# Write a Program to add two integers >0 without using the plus operator
def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print(add_nums(num1,num2))