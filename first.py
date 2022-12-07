# print("samad")
# i = input()
# print ("my name is " + i)
# i += " is a girl"
# print(i)
# import string

# y = string(input())
# y += "  is my age."
# print(y)

"""boolean"""

# print(3 == 9)
# print(3 != 9)
# print(3 > 9)
# print(3 >= 9)
# print(3 < 9)
# print(3 <= 9)
# if and else statements
# n = int(input())
# if n == 1:
#     print("one")
# elif (n==1 or n==2):
#     print ("one or two.")
# else:
#  print("not allowed")
# print (1==1 and 2==2)
# #print()
# #print()
# #print()
# n = int(input())
# if n == 1:
#     print("1 is the hidden number")
# elif n == 1 or n == 2:
#     print("2 is the hidden number.")
# else:
#     print("this can't work")
# print()
# print()
# print()
# a= input()
# b= input()
# c= input()
# d= input()
# if (( int(a) > 10 or int(b) > 10) or (int(c) > 10 or int(d) > 10)):
#     print("too high")
# elif (a==b and c==d):
#     print("correct")
# elif (a==b or b==c):
#     print("half")
"""indexing"""
"""intergers or values of a list can also be indexed 
out from either the begining or the end"""

"""multiple conditions"""

"""#lists"""
# words= ["hello", "world", "!"]
# empty_lists= []
# print(words[0])
# print(words[1])
# print(words[2])
"""string can also contain all types of variable types,
 for eiample:"""
# num = 23
# things= [ "words", 45, [ 2,"sat",num]]
# print (things[0])
# print (things[1])
# print (things[2][0])
# print (things[2][1])
# print (things[2][2])
"""string can also be indented like lists,
 eg:"""
# word= "hello world"
# print (word[0])
# print (word[1])
# print (word[2])
# print (word[3])
# print (word[4])
"""lists can also be reassigned , eg:"""
# num =[4,"red",4,4]
# num[3]= 5
# print(num[3])

"""append"""
# num = ["samad"]
# i = input()
"""#append alllows u to append any item to the end of a list """
# num.append(i)
# print(num[1])
"""insert allow you to insert any item to any part of a list.
"""
# num.insert(index,"olalekan")
# num.insert(1,"Busari")
# print(num)
# print(len(num))
"""
the values of a list can also be removed with the remove keywork"""
# items= ["eggs","yam","rice",45,565.3,"palmoil"]
# print(items)
# items.remove("eggs")
# print(items)
"""the values of a list can also be rearranged with the reverse keywork,
it would display them from last to the begining"""
# items = ["eggs", "yam", "rice", "palmoil"]
# print(items)
# items.reverse()
# print(items)
"""the intergers of a list can also be rearranged with the sort keywork,
it would display them in assending order"""
# items= [1,45,565.3,74.5,0.45]
# print(items)
# items.sort()
# print(items[:3])

# items = 'samad,emanuel,bolu'
# print(items)

# j = items.split()
# print(j)

# joiner = ' and '.join(j)
# print(joiner)

"""while loop"""
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(str(i))
#     else:
#         print(str(i) + "is odd")
#     i += 1
# print("finish")

"""break is used to break a loop prematurely"""
i = 2
while True:
    print(i)
    i += 1
    # if i >= 10:
    #     print(" breaking ")
    #     break
print("program finished")

"""continue statement"""
# i = 2
# while i<= 20:
#     print(i)
#     i+=1

#     if i %5 ==0:
#         print(".")
#         continue
# print("program finished")

"""for loop"""
# words=["bread","egg","beans"]
# for item in words:
#     print(item + "!")


# myName = "samadOlalekan"
# counter = 0

# for letters in myName:
#     if letters == "z" or letters == "y":
#         counter += 1

# print(counter)
# if counter == 0:
#     print("there are none found")
"""range
range prints numbers from 0 to the the specified numeber
to output its contents , it must first be converted to a list
using the list() function"""
# numbers = list(range(20))
# print(numbers[12])
# list_of_numbers= list(range(290))
# print(list_of_numbers)
"""the range of a list can also be specified, from initial to final.
"""

# numbers= list(range(3,8))
# print(numbers)

# they are both the same
# print(range(20) == range(0,20))

"""the first  variable represent the initial number
#the second is the ending 
#the third is the multiples of the range"""
# numbers = list(range(0, 21, 4))
# print(numbers)

# students = ["samad", "Emanuel", "bolu", "manuel"]
# for people in range(0, len(students)):
#     if people == 4:
#         break
#     else:
#         print(students[people])

#         print("counter is " + str(people))

"""functions
funcions are decleared with the keywork DEF"""
# For example:
# this line would declear the function
# def hello():
#     print("hello world")

"""this line would print the function"""
# hello()

"""some function also take in arguments , for example:"""
# def emanuel(age, likes):
#     print( "emanuel is " + str(age) + "years old and he likes " + likes)

# emanuel(23, "games")

"""return key work"""
# def max(x, y):
#     if x>= y:
#         return x
#     else :
#         return y

# print(max(4,6))
#
#
"""functions can also be varibles of other functions , for example:"""


def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 4
b = 5
print(do_twice(add, a, b))

"""modules"""
"""piece of code written by other people for a specified task"""
# import random
"""random helped print 5 random numbers from the random key"""
# for i in range(10):
#     value = random.randint(1,6)
#     print(i)

"""casting"""
"""to set any variable to another data type 
we use casting in python"""
# for example:
# float(56)
# int(45.6)
# string(samad)
# bool(0)#this would displat false,cos the number is a negative.
"""you can also print single letters from a string ,
for example:"""
# name = "samad"
# print(name[0])
# print(name[1])
# p9rint(name[2])
# print(name[3])
# print(name[4])
