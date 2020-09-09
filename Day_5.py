"""

list1 = [1,2,3,4,5]
#[1,4,9,16,25]

list2 = []
for item in list1:
  list2.append (item*item)

list1 = [1,2,3,4,5]
#[1,4,9,16,25]
#list comprehension
list3 = [item*item for item in list1]

names = ['India','Bharat','Bharath']

print ([len(name) for name in names])

print ([len(name) for name in names])

names = ['India','Bharat','Bharath']

dict1 = {}

for name in names:
  dict1[name] = len(name)

#dictionary comprehension

print ({name: len(name) for name in names})



list1 = [1,2,3,4,5]
#map functionality

def f1(x):
  return (x*x*x)

print (list(map(f1, list1)))
print (list(map(lambda x : x*x*x, list1)))

names = ['India','Bharat','Bharath']
def f2(str1):
  return (len(str1))


print (list(map(f2, names)))
print (list(map(lambda str1: len(str1) , names)))

list1 = [1,2,3,4,5]

def iseven(x):
  return (x % 2 == 0)
   

print (list(map(iseven, list1)))
print (list(filter(iseven, list1)))
print (list(filter(lambda x: x % 2 == 0, list1)))

"""

#reduce

list1 = list(range(10, 0, -1))


def f3(x, y):
    return (x * y)


import functools
print(functools.reduce(f3, [1, 2, 3, 4, 5]))

#map reduce
#Indian Engineer - Google USA
#Sanjay Ghemawat
#Hadoop
#Spark
#Datbrick
