# 21.	Fibonacci Generator: Write a program that generates the Fibonacci sequence up to n terms using a while loop.
# n1=0
# n2=1
# user_input=int(input('ENter a num = '))
# i=0
# print(n1)
# print(n2)
# while i<user_input:
#     nxt_num = n1+n2
#     n1=n2
#     n2=nxt_num
#     print(nxt_num)
#     i+=1
    
# 22.	Second Largest: Find the second largest number in an unsorted list without sorting the list first.

# num=[1,2,3,88,6,4,3,54,76,4,23,6]
# max=0
# sec_max=0
# for i in num:
#     if i>max:
#         max=i
# num.remove(max)
# for i in num:
#     if i>sec_max:
#         sec_max=i
# print(max)
# print(sec_max)

# 23.	FizzBuzz: Loop from 1 to 50. If a number is divisible by 3, print "Fizz". By 5, print "Buzz". By both, print "FizzBuzz". Otherwise, print the number.

# for i in range(1,52):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)
# 24.	Word Frequency: Given a sentence, count how many times each specific word appears using lists and sets
# sentence = 'Ahmad is a good boy and boys like ahmad are very good and hardworking a a '

# words = sentence.lower().split()
# unique_words=set(words)
# for i in unique_words:
#     print(f'{i} count is : {words.count(i)}')

# 25.	The Common Denominator: Find all numbers between 100 and 500 that are perfectly divisible by both 4 and 7.
# num=[]
# for i in range(100,501):
#     if i%4==0 and i%7==0:
#         num.append(i)
# print(num)

# 26.	List Merger: Take two sorted lists and merge them into a single, correctly sorted list.

# l1=[1,2,3,4,5,6,7,8,9]
# l2=[4,5,7,8,3,4,5,2,1]
# l1.extend(l2)
# l1.sort()
# print(l1)

# 27.	Password Validator: Write a script that checks a string to ensure it has at least 8 characters, contains at least one number, and one uppercase letter.

# password = input('Enter Your Password = ')

# if len(password)>=8 and any(word.isdigit() for word in password) and any(word.isupper() for word in password):
#     print('valid')
# else:
#     print('invalid')

# 28.	Matrix Flattener: You have a 2D list (e.g., [[1, 2], [3, 4]]). Use nested for loops to flatten it into a 1D list ([1, 2, 3, 4]).
# new=[]
# for i in matrix:
#     for m in i:
#         new.append(m)

# print(new)
# matrix = [[1, 2], [3, 4]]
# matrix=[m for item in matrix for m in item]
# print(matrix)

# 29.	Set Disjoint: Check if two different sets of server IP addresses have absolutely no addresses in common.
# one={1,2,3,4}
# two={5,6,7,8,4}

# print(one.isdisjoint(two))

# 30.	Symmetric Difference: Find the data points that are in Set A or Set B, but not in both.
# one={1,2,3,4}
# two={5,6,7,8,4}
# print(one.symmetric_difference(two))

# 31.	Digit Extractor: Loop through a string like "Pyth0n 1s Awe5ome" and extract only the numbers to calculate their sum.

# sentence = "Pyth0n 1s Awe25ome"
# sum =0

# for i in sentence:
#     if i.isdigit():
#         sum +=int(i)

# print(sum)
    
# 32.	Longest Word: Write a program to find and print the longest word in a given sentence.
# sentence = 'Ahmad is a good boy and boys like ahmad are very good and hardworking a a whatalongword '
# words=sentence.split()
# longest=''
# for i in words:
#     if len(i)>len(longest):
#         longest=i
# print(longest)

# 33.	Interactive Calculator: Create a while loop that keeps running a calculator program until the user types "exit". It should ask for two numbers and an operator (+, -, *, /).
# end=''
# while end!='exit':
#     inp1=int(input('enter num 1 ='))
#     inp2=int(input('enter num 1 ='))
#     opt1=input('Enter operator like = ').lower()
#     if opt1 == '+':
#         print(inp1+inp2)
#     elif opt1 == '-':
#         print(inp1-inp2)
#     elif opt1 == '/':
#         print(inp1/inp2)
#     elif opt1 == '*':
#         print(inp1*inp2)
#     end=input('Enter exit to end else anything to continue = ')
# print('exited')

# 34.	Prime Finder: Write a program with nested loops to generate a list of all prime numbers up to 100.
# list_prime=[]
# for num in range(1,101):
#     fac=0
#     for i in range(1,num+1):
#         if num%i==0:
#             fac+=1
#     if fac==2:
#         print(num)

# 35.	The Guessing Game: Set a secret number. Give the user 3 tries to guess it using a while loop and if/elif statements to give "too high" or "too low" hints.

# num=12
# tries=3

# while tries>0:
#     user_guess=int(input('Enter a number to guess = '))
#     if user_guess>num:
#         print('the num is lower')
#     elif user_guess<num:
#         print('num is graeter')
#     elif user_guess==num:
#         print('You found it bro ')
#         break
#     tries-=1

# 36.	Three-Way Intersection: Find the common elements shared across three completely different lists.

# a=[1,2,3,4,5]
# b=[1,2,3,8,9]
# c=[1,2,3,6,8]

# final = list(set(a)&set(b)&set(c))

# print(final)

# 37.	Alphabetical Grouper: Take a list of names and write logic to group them into lists based on their starting letter.
# names=['Ahmad','basit','cane','john','Ali','bashir','A']
# directory={}

# for name in names:
#     fir_let=name[0].upper()

#     if fir_let not in directory:
#         directory[fir_let]=[]

#     directory[fir_let].append(name)

# print(directory)


# 38.	List Rotation: Rotate a list of numbers to the right by k positions (e.g., [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3]).    

# num = [4,5,1,2,3]

# for _ in range(2):
#     last=num.pop()

#     num.insert(0,last)

# print(num)