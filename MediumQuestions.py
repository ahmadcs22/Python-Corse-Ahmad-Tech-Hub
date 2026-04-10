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