#tuple and declaration with single item 
#access tuple with exsist element 
#tuple conversion to list and list to tuple 
#del to delete tuple 
#ctrl+alt+N
# my_tup=(1,2,3,4,5)

# hello = (1,)

# hi = tuple((1,2,3,"hello"))

# # print(type(my_tup))
# # print(type(hello))

# print(type(hi))

names=('0,Ahmad','1.ali','2.haniya','3.aleena')

# if '0,Ahmad' in names:
#     print("we found ahmad")

names_list= list(names)
names_list.remove('2.haniya')
names=tuple(names_list)

# del names


print(names)