## Codility ##

Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    A = [int(i) for i in A] # convert items to int
    A = sorted(set(A)) # convert list to sorted set
    if max(A) > 0 :
        for i in range(0, len(A)-1):
            #print(A[i])
            if (A[i+1] - A[i] > 1) :
                return int(A[i]+1)

        return int(max(A)+1)

        #return int(max(A) + 1)
    elif max(A) <= 0 :
        #return int(max(A) + abs(max(A)) + 1)
        return int(1)

#===============================================================================
## Write a function ##
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
  The year can be evenly divided by 100, it is NOT a leap year, unless:
    The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if  year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))

#===============================================================================
## Print Function ##
Read an integer N.

Without using any string methods, try to print the following:
123...N

if __name__ == '__main__':
    n = int(input())

    print(*range(1, n+1), sep='')

#===============================================================================
## palindromic integers ##

You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.
Explanation

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.
n = int(input())
list = input().split(" ")

def palindrom(num):
    return str(num) == str(num)[::-1]

print(all(int(i)>=0 for i in list) & any(palindrom(i) for i in list))
#===============================================================================
## Second largest number ##

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


    def second_largest(numbers):
        m1 = max(numbers)
        m2 = -float('Inf')
        for i in range(n):
            if arr[i] != m1 and arr[i] > m2:
                m2 = arr[i]
        print(m2)

second_largest(arr)

#===============================================================================

## Second smallest ##

def second_smallest(numbers):
    first, second = float('inf'), float('inf')
    for x in numbers:
        # If current element is smaller than first then
        # update both first and second
        if x < first:
            second = first
            first = x

        # If arr[i] is in between first and second then
        # update second
        elif (x < second and x != first):
            second = x

    return second
print(second_smallest([1, 2, -8, -2, 0]))
print(second_smallest([0,1,2,3]))
print(second_smallest([-3,-2,-1]))


#===============================================================================
## Second smallest in Nested Lists ##
Find the second samllest number in a nested list composed of name and score.

if __name__ == '__main__':

    python_students_list = []
    score_list = []
    lowest_name = []

    for item in range(int(input())):
        name = input()
        score = float(input())

        python_student = [name,score]
        python_students_list.append(python_student)
        score_list+=[score]
    lowest_score = sorted(score_list)[1]

    for a,b in sorted(python_students_list):
            if b==lowest_score:
                print(a)

#===============================================================================
#===============================================================================
#-#=======#-#
## Strings ##
#-#=======#-#

## Swap Case ##

You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa.
Pythonist 2 → pYTHONIST 2


def swap_case(string):
    result = ""
    for s in string:
        if s.islower():
            result+=s.upper()
        elif s.isupper():
            result+=s.lower()
        else:
            result+=s
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#===============================================================================
## format print ##

You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#===============================================================================
## Mutable string ##
Read a given string,
change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    string = ''.join(str_list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#===============================================================================
## Probe for substring in string ##

def count_substring(string, sub_string):

    count = 0
    #Greedy, check each portion starting from index 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
#===============================================================================
## alpha / digit counter ##

# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

string = input("Enter string: ")
def alpha_digit_calc(string):
    alpha_cnt = 0
    digit_cnt = 0
    for char in string:
        if char.isalpha():
            alpha_cnt+=1
        elif char.isdigit():
            digit_cnt+=1
        else:
            pass
    return "Letters count is {}, Digit count is {}".format(alpha_cnt, digit_cnt)

print(alpha_digit_calc(string))

#===============================================================================

## String Validators ##

In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
    i = 1
    while(i < 6):
        if i == 1:
            print(any([char.isalnum() for char in s]))
        elif i == 2:
            print(any([char.isalpha() for char in s]))
        elif i == 3:
            print(any([char.isdigit() for char in s]))
        elif i == 4:
            print(any([char.islower() for char in s]))
        elif i == 5:
            print(any([char.isupper() for char in s]))
        i+=1
#===============================================================================
## Formatting string ##
Given a decimal number, print the int, oct, hex and bin starting from 1 till that number.

def print_formatted(number):
    i = 1
    while i <= number:
        print("{}  {}  {}  {}".format(int(i), int(oct(i)[2:]), int(hex(i)[2:]), int(bin(i)[2:])))
        i+=1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#===============================================================================
## Capitalize (dynamic n words) ##
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.


# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    result = ""
    for i in range(0,len(words)):
        result+=(words[i].capitalize() + " ")
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#===============================================================================
## Word frequency count ##

# Enter your code here. Read input from STDIN. Print output to STDOUT

l={}
for i in range(int(input())):
    x=input()
    if x not in l:
        l[x]=1
    else:
        l[x]=l[x]+1
print(len(l))
for i in l:
    print(l[i],end=" ")

# Another solution order dict #

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

## Frequency of numbers ##

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

#===============================================================================
## Subtract the Product and Sum of Digits of an Integer ##

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product= 1
        sum = 0
        for i in n.strip():
            sum += int(i)
            product *= int(i)
        return product - sum


#===============================================================================

#-#========================#-#
## Conditional flow & Loops ##
#-#========================#-#
## two diemnsional array ##

Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Input
Input number of rows: 3
Input number of columns: 4
Output
[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

l = [[0 for col in range(columns)] for row in range(rows)]
# i.e 3 rows & 4 columns [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(rows):
    for j in range(columns):
        l[i][j] = i*j
print(l)

#===============================================================================
## Pyramid loop ##

# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

n  = int(input("Enter a number: "))


for i in range(1,n+1):
    for j in range(i):
        print(i, end="")
    print("\t")

## Another solution ##

for i in range(1,n+1):
    print(str(i) * i)
#===============================================================================
## Asterisk pattern ##

#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

from math import ceil
n = 5

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print("\t")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\t")

#===============================================================================
#===============================================================================
#-#=====#-#
## Lists ##
#-#=====#-#

## listToString ##
# Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

#===============================================================================
## Subquery probe ##

def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

#===============================================================================
## common items in a list ##

Write a Python program to find common items from two lists.
input
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
output
{'Green', 'White'}

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

def intersection(l1,l2):
    result = []
    for item in l1:
        if item in l2:
            result.append(item)
    return result

print(intersection(color1,color2))

# Another solution

print(set(color1) & set(color2))

# For difference

#===============================================================================
##  Replace Elements with Greatest Element on Right Side ##

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

arr: [17,18,5,4,6,1]
it1: [18,18,5,4,6,1]
it2: [18,6,5,4,6,1]
it3: [18,6,6,4,6,1]
it4: [18,6,6,6,1,1]
it6: [18,6,6,6,1,-1]

def replaceElements(arr: List[int]) -> List[int]:
    for i in range(0,len(arr)-1):
        max_no = -float("Inf")
        for j in range(i+1,len(arr)-1):
            if arr[j] > arr[j+1] and arr[j] > max_no:
                max_no = arr[j]
        if i < len(arr)-2:
            arr[i] = max_no
        else:
            arr[i] = arr[i+1]
            break
    arr[-1] = -1
    return arr
#===============================================================================

#===============================================================================
#-#==========#-#
## Dictionary ##
#-#==========#-#

## Key dictionary ##

# Check if a given key already exists in a dictionary
# input
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(5)
# is_key_present(9)
# output
# Key is present in the dictionary
# Key is not present in the dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_presenet(k):
        if k in d.keys():
            print("Key {} is presnt in the dictionary".format(k))
        else:
            print("key {} is not present in the dictionary".format(k))

is_key_presenet(5)
is_key_presenet(9)

#===============================================================================
## Sort dictionary values asc or desc ##

# import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(0))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
# print('Dictionary in descending order by value : ',sorted_d)

def sort_dict_values(d, asc = True):
    l = []
    for k,v in d.items():
        t = k,v
        l.append(t)
        if asc == True:
            l = sorted(l, reverse=False)
        else:
            l = sorted(l, reverse=True)
    print(l)

sort_dict_values(d, asc=False)
#===============================================================================

#===============================================================================

#===============================================================================
