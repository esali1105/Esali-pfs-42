Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #aissgnment
>>> a=4
>>> b=5
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+=b
>>> a
9
>>> a-=b
>>> a
4
>>> a*=b
>>> a
20
a**=b
b
5
a%=b
a
0
a//=b
a
0
a/=b
a
0.0
#
a=5
b=6
a+=b
b
6
a-+b
5
a-=b
b
6
a/=b
b
6
a//=b
b
6
a**=b
b
6
a*=b
b
6
a%=b
b
6
#comparison
a=6
b=9
a>b
False
a<b
True
b>a
True
b<a
False
a<=b
True
a>=b
False
a=b
a==b
True
b<=a
True
b>=a
True
#logical
a=10
b=20
a<b and a>b
False
a<b and b>a
True
a<=b and b>=a
True
a>=b and b<=a
False
a!=b or a==b
True
a<b or b>a
True
a<=b or b>=a
True
not True
False
not False
True
#identify
a=3
type
<class 'type'>
type(a) is int
True
type(a) is not int
False
type(a) is not float
True
tpye(a) is not bool
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tpye(a) is not bool
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
type(a) is not bool
True
type(a) is not str
True
type(a) is str
False
type(a) is complex
False
type(a) is not complex
True
#membership
a=1,2,3,4,5,6,7,8,9,10
9 in a
True
15 in a
False
20 not in a
True
#bitwise
a=4
b=7
bin(4)
'0b100'
bin(7)
'0b111'
a&b
4
a=3
b=6
a&b
2
bin(3)
'0b11'
bin(6)
'0b110'
a=2
b=5
a|b
7
a=3
b=7
a|b
7
a=5
b=7
a|b
7
a=2
b=4
a|b
6
a=5
-(a+1)
-6
b=-8
-(a+1)
-6
~b
7
a=3
b=7
a
3

a=3
b=7
a^b
4
a=9
b=7
a^b
14
a=4
a<<2
16
bin(4)
'0b100'
a=8
a>>3
1
a=8
a<<3
64
