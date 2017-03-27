# -*- coding: utf-8 -*-

__author__ = 'Sky Hai'

#Python viriable type

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
##General Operation

###Index

###Slice

###Sequence

###Multiple

###Membership

###Length, Max and Min

##Declaration

##Special Operation

##Function


#Python Tuple
##General Operation

###Index

###Slice

###Sequence

###Multiple

###Membership

###Length, Max and Min

##Declaration

##Special Operation

##Function

#Python Set
##General Operation

###Index

###Slice

###Sequence

###Multiple

###Membership

###Length, Max and Min

##Declaration

##Special Operation

##Function

#Python Dict
##General Operation

###Index

###Slice

###Sequence

###Multiple

###Membership

###Length, Max and Min

##Declaration

##Special Operation

##Function

