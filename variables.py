Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name="esali"
>>> print(name)
esali
>>> print("name")
name
>>> city="vijayawada"
>>> print(city)
vijayawada
>>> a=4
>>> c=8
>>> print(a+c)
12
>>> fname="sai"
>>> lname="pala"
>>> print(fname+""+lname)
saipala
>>> a=3,b=4
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=3;b=4
>>> print(a+b)
7
>>> a,b=6,7
>>> print(a+b)
13
>>> a=4
>>> b=6
>>> print(a+b)
10
>>> @=9
SyntaxError: invalid syntax
>>> $=7
SyntaxError: invalid syntax
_=40
print(_)
40
_a=22
print(_a)
22
if=10
SyntaxError: invalid syntax
while=33
SyntaxError: invalid syntax
a,b,c=1,2,4
print(a,b,c)
1 2 4
a=1,2,3,4,5
print(a)
(1, 2, 3, 4, 5)
a,b,c=1,2,3,4,5,6
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,b,c=1,2,3,4,5,6
ValueError: too many values to unpack (expected 3, got 6)
p
first name="sai"
SyntaxError: invalid syntax
first_name="sai"
print(first_name)
sai
firstname="sai"
print(firstname)
sai
 b=11
 
SyntaxError: unexpected indent
a=(1,2,3,4)
print(a)
(1, 2, 3, 4)
a,b,c=(1,2,3)
print(a,b,c)
1 2 3
a=33
print
<built-in function print>
a=22
print(a)
22
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
#casesensitive
name="sai"
print(name)
sai
Name="sai"
print(Name)
sai
NAME="sai"
print(NAME)
sai
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
