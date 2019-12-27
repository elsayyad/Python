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
## Nested Lists ##
Find the second lowest number in a nested list composed of name and score.

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
#===========#
## Strings ##
#===========#

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
