'''
Puzzle taken from leetcode.com

You are given a number of lists representing numbers.
For example, the number 204 would be the list [4,0,2]

Write a program that can two more of these lists, add their representative numbers together,
and return a list of the same form.
'''
import math

def list2num(l):
    n = 0
    for i in range(len(l)):
        n += 10**i * l[i]
    return n

def num2list(n):
    l = []
    
    num_digits = round(math.log(n, 10))
    for power_of_ten in range(num_digits):
        tens_place_above_current_digit = 10**(power_of_ten+1)
        rest_of_number = (n // tens_place_above_current_digit) * tens_place_above_current_digit
        current_num = n - rest_of_number
        digit = int(current_num / 10**(power_of_ten))

        l.append(digit)
        n -= current_num

    return l

l1 = [5,6,4]
l2 = [3,2,1,4,6]

n1 = list2num(l1)
n2 = list2num(l2)

n3 = n1 + n2
l3 = num2list(n3)
print(l3)