# Functions (Write Cleaner Code)
# o	Content: The def keyword. Parameters vs. Arguments. The return statement.


# def sum(a,b):
#     print(a+b)

# sum(10,20)

# f'{}'
# def student(name,dept,uni='uog'):
#     print(f'{name} is from {dept} of uni {uni}')

# student(uni='uog',name='ahmad',dept='cs')


# positional / keyword based

def add(a,b,c,/):
    return a+b+c

print(add(10,29,30))


