# -*- coding: utf-8 -*-

'''
@author: Sky Hai
@contact: hsssgddtc@hotmail.com
@file: 01.data_type.py
@time: 2017/3/27 17:46
@desc: Python variable type
'''


#Python number，python3 supports three kinds of types: int, float and complex
var1 = 10; #int
var2 = 12.34;#float
var3 = 123j #complex
var4 = 123+45j #complex

print(var1)
print(var2)
print(var3)
print(var4)
print(var3+var4)

print(type(var1))
print(type(var2))
print(type(var3+var4))

#Python string
str_1 = "I love Python"
##General Operation
###Index
print(str_1[0])

###Slice
print(str_1[2:6])
print(str_1[2:])
print(str_1[2::2])
print(str_1[-4:])
print(str_1[-3:-1])

###Sequence/Concatenate
print(str_1+str_1)

###Multiple
print(str_1*2)

###Membership
print('l' in str_1)

###Length, Max and Min
print(len(str_1))
print(max(str_1))
print(min(str_1))

##Details
###Single quote string and Escape quotes
str_2 = 'Let\'s go'
print(str_2)
str_3 = "Let's go"
print(str_3)

###String expression
print(str(str_2))
print(repr(str_2))

###Special string
str_l = """
This is a very long string.
And just for testing~
"""
print(str_l)
str_or = "Hello \n World~"
str_r = r"Hello \n World~"
print(str_or)
print(str_r)
str_ou = '这是一个测试字符串'
str_u = u'这是一个测试字符串'
print(str_ou)
print(str_u)

##Format string
###Format Operator

###Auxiliary Format Operator

###Escape sequence

##Function
###Split
####Return list
print(str_1.split(" "))
print(str_1.split(" ",1))
print(str_1.rsplit(" ",1))
print(str_or.splitlines(True))
print(str_or.splitlines(False))

####Return string
lis_1 = ['I', 'love', 'Python']
print(" ".join(lis_1))

####Return tuple
print(str_1.partition(" "))
print(str_1.rpartition(" "))

###Search
###Return -1 if not found
print(str_1.find("o"))
print(str_1.rfind("o"))
print(str_1.find("o",4,11))
print(str_1.find("z"))

###Return error if not found
print(str_1.index("o"))
print(str_1.rindex("o"))
#print(str_1.index("o",4,11))

###Space remove
print('     '+str_1+'     '.strip())
print('     '+str_1+'     '.lstrip())
print('     '+str_1+'     '.rstrip())

###Caps
print(str_1.lower())
print(str_1.islower())
print(str_1.upper())
print(str_1.isupper())
print(str_1.title())
print(str_1.istitle())
print(str_1.capitalize())
print(str_1.swapcase())

###Judgement
print(str_1.isalnum())
print(str_1.isalpha())
print(str_1.isdecimal())
print(str_1.isdigit())
print(str_1.isnumeric())
print(str_1.isspace())
print(str_1.startswith("I",4,11))
print(str_1.endswith("n",3,4))

###Encoding
print(str_u.encode("utf-8",errors='stric'))
print(str_u.encode("utf-8").decode("utf-8"))

###Replace
print(str_1.replace(" ",","))
tbl = str.maketrans(" ",",")
print(str_1.translate(tbl))
print(str_1.replace(" ","\t").expandtabs(3))

###Fill
print(str_1.center(40,'*'))
print(str_1.ljust(40,'*'))
print(str_1.rjust(40,'*'))
print(str_1.zfill(40))

###Count
print(str_1.count('o',3,11))

#Python List
##Declaration
list_1 = [1,2,3,4,5,6]
list_2 = list((7,8,9,1,2,4))
##General Operation
###Index
print(list_1[3])

###Slice
print(list_1[2:4])
print(list_1[0:3:2])
print(list_1[-3:-1])

###Sequence
print(list_1+list_2)

###Multiple
print(list_1*2)

###Membership
print(3 in list_1)
print('a' in list_1)

###Length, Max and Min
print(len(list_2))
print(max(list_2))
print(min(list_2))

##Special Operation
###Update
list_1[3] = 7
print(list_1)
list_1[2:4] = list_2
print(list_1)

###Delete
del list_1[3]
print(list_1)

##Function
list_1.append(10)
print(list_1)
print(list_1.count(1))
list_1.extend(list_2)
print(list_1)
print(list_1.index(9))
list_1.insert(4,11)
print(list_1)
print(list_1.pop(4))
print(list_1)
list_1.remove(9)
print(list_1)
list_1.reverse()
print(list_1)
list_1.sort(reverse=True)
print(list_1)

#Python Tuple
##Declaration
tup_1 = (1,2,3,4,5,6)
tup_2 = tuple([7,8,9,1,2,4])
##General Operation
###Index
print(tup_1[3])

###Slice
print(tup_1[2:4])
print(tup_1[0:3:2])
print(tup_1[-3:-1])

###Sequence
print(tup_1+tup_2)

###Multiple
print(tup_1*2)

###Membership
print(3 in tup_1)
print('a' in tup_1)

###Length, Max and Min
print(len(tup_2))
print(max(tup_2))
print(min(tup_2))

##Special Operation
### Delete
#del tup_1
#print(tup_1)

#Python Set
##Declaration
set_1 = {1,2,3,4,5,6}
set_2 = set((3,4,5,6,7,8))
##General Operation
###Compare
print(set_2 in set_1)
print(set_2 not in set_1)
print(set_2 == set_1)
print(set_2 != set_1)
print(set_2 < set_1)
print(set_2 <= set_1)
print(set_2 > set_1)
print(set_2 >= set_1)

###Relation
print(set_1&set_2)
print(set_1|set_2)
print(set_1-set_2)
print(set_1^set_2)
set_1&=set_2
print(set_1)
set_1|=set_2
print(set_1)
set_1-=set_2
print(set_1)
set_1^=set_2
print(set_1)

##Function
set_1 = {1,2,3,4,5,6}
set_2 = set((3,4,5,6,7,8))
###All sets
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.symmetric_difference(set_2))
print(set_1.copy())

###Mutable sets
set_1.update(set_2)
print(set_1)
set_1.intersection_update(set_2)
print(set_1)
set_1.difference_update(set_2)
print(set_1)
set_1.symmetric_difference_update(set_2)
print(set_1)
set_1.add(9)
print(set_1)
set_1.remove(9)
print(set_1)
set_1.discard(9)
print(set_1)
print(set_1.pop())
print(set_1)
set_1.clear()
print(set_1)

#Python Dict
##Declaration
dict_1 = {"key1":"value1",12:34,'key2':'value2'}
##General Operation
###Index
print(dict_1["key1"])

###Assignment
dict_1[56]=78
print(dict_1)

###Delete
del dict_1[56]
print(dict_1)

###Membership
print(12 in dict_1)

###Length, Max and Min
print(len(dict_1))
#print(max(dict_1))
#print(min(dict_1))

##Function
print(dict_1.get(12))
print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())
print(dict_1.pop("key1"))
print(dict_1)
print(dict_1.popitem())
print(dict_1.fromkeys(tup_1))
dict_2 = {"key1":"value1",1:34,'key2':'value2'}
dict_1.update(dict_2)
print(dict_1)

##Copy and Deepcopy
"""
1.copy() will only copy the father object and not its children
2.deepcopy() will copy both the father and children object
"""
import copy
a = [1, 2, 3, 4, ['a', 'b']]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(5)
a[4].append('c')

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
