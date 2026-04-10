# 1.	The Counter: Write a for loop that prints all numbers from 1 to 100.
# for i in range(1,101):
#     print(i)
# 2.	The Countdown: Write a while loop that counts backward from 10 to 1, then prints "Liftoff!".
# floor=10
# while(floor>0):
#     print(floor)
#     floor -=1
# print('lift off')

# 3.	Even or Odd: Take a number as input and use an if/else statement to check if it's even or odd.
# number=int(input('Enter a num = '))
# if number%2==0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')
# 4.	List Summation: Given a list of numbers (e.g., [4, 7, 2, 9]), calculate the total sum without using the built-in sum() function.
# num = [1,2,4]
# total = sum(num)
# print(total)

# 5.	Vowel Counter: Loop through a string and count how many vowels (a, e, i, o, u) it contains.
# vowels = ('a','e','i','o','u')
# inp=input('Enter a strng = ').lower()
# num_count=0
# for i in inp:
#     if i in vowels:
#         num_count+=1

# print(f'{num_count} vowels')

# 6.	String Reverser: Reverse a string using slicing (e.g., word[::-1]).

# string='ahmad'

# print(string[::-1])

# 7.	Palindrome Checker: Check if a given word reads the same forward and backward (like "radar" or "level").

# string='alla'

# if string == string[::-1]:
#     print('reverse and forward same')
# else:
#     print('not same ')

# 8.	List Modifier: Create a list of 5 tech skills. Append a new skill to the end, and remove the first skill.

# skills =['python','django','react','AI','ML']

# skills.append('Deep Learning')
# skills.remove(skills[0])
# print(skills)

# 9.	Tuple Conversion: Create a tuple of 3 numbers. Since tuples are locked, convert it to a list, change the second number, and convert it back to a tuple.

# num=(1,2,3)

# num_list=list(num)

# num_list[1]=99

# num = tuple(num_list)

# print(num)

# 10.	The Filter: Write a loop that prints only the positive numbers from [-5, 3, -1, 10, -8, 2].
# numbers=[-5, 3, -1, 10, -8, 2]
# for i in numbers:
#     if i>0:
#         print(i)
#     continue

# 11.	Duplicate Destroyer: Take a list with duplicate items and use a set to remove all duplicates.

# list_of_num=[1,2,3,4,5,5,4,3,2,1]
# rem=set(list_of_num)
# list_of_num=list(rem)
# print(list_of_num)

# 12.	Set Intersection: Given two sets of student IDs, find the IDs that exist in both sets.

# set1={100,101,97,102}
# set2={97,98,67,89,99}

# same_id = set1.intersection(set2)

# print(same_id)

# 13.	List Concatenation: Combine two different lists into a single list without using the .extend() method.

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]

# combined=[*list1,*list2]

# print(combined)

# 14.	The Multiplier: Use a for loop to multiply every number in a list by 3 and print the new values.

# list_num=[2,4,6,8,10]
# new_list=[]
# for i in list_num:
#     new_list.append(i*3)

# print(new_list) 

# 15.	The Breakout: Loop through numbers 1 to 20. If you hit the number 13, use break to stop the loop completely.

# for i in range(1,21):
#     print(i)
#     if i==13:
#         break
# print('13 occured loop out ')

# 16.	The Skipper: Loop through numbers 1 to 20. Use continue to skip all numbers divisible by 3.
# for i in range(1,21):
#     if i%3==0:
#         continue
#     else:
#         print(i)

# 17.Access Control: Take a user's age as input. Print "Access Granted" if they are 18 or older, and "Access Denied" if younger.

# age = int(input('enter your age = '))
# if age >=18:
#     print('access granted')
# else:
#     print('access denied')

# 18.	Variable Swap: Swap the values of two variables (a = 5, b = 10) without creating a third temporary variable.
# a=5
# b=10

# a=a^b
# b=a^b
# a=a^b

# print(a,b)

# 19.	Tuple Search: Write a program that checks if a specific target number exists inside a tuple.

# numbers=(1,2,3,4,5,6,7,8,9,10)
# inp=int(input('enter a num = '))

# if inp in numbers:
#     print('found')
# else:
#     print('not found')

# 20.	Format Cleaner: Take a string with messy spacing (e.g., " Python ") and use string methods to strip the spaces and convert it to completely lowercase.
# inp=input('enter a string = ')
# cleaned=inp.strip().lower()
# print(cleaned)