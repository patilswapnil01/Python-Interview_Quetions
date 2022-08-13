# Python program to print Fibonacci series program in using Iterative methods

from re import I
from unittest import result


first = 0
second = 1
n = int(input("Hit the range here : "))
for i in range(0,n):
    if i<=1:
        result=i
    else:
        result = first + second
        first = second
        second = result
    print(result)