#conditions
#if condition by using camparision operators
#<,>,<=,>=,!=,==
'''a=10
b=15
if a<=b:
    print("true")'''


'''a=5
b=15
if a>=b:
    print("true")'''

'''a=30
b=15
if a<b:
    print("true")'''

'''a=6
b=15
if a!=b:
    print("true")'''

'''a=20
b=19
if a==b:
    print("true")'''

'''a=int(input("a value is"))
b=int(input("b value is"))
if a<b:
    print("less")'''

'''a= int(input("a value"))
if a>7:
    print("less")'''

'''a="python"
if a!="python":
    print("match")'''

'''a="python"
if a=="python":
    print("match")'''

'''a="python"
if a!="java":
    print("match")'''


#if condition by using logical operators
#and , not ,or

'''a=10
b=7
if a<b and b>a:
    print("less")'''


'''a=5
b=7
if a!=b and a==b:
    print("less")'''


'''a=9
b=12
if a<b or b>a:
    print("true")'''


'''a=4
b=9
if a!=b or a==b:
    print("true")'''


'''a=10
b=20
if not a<b and b>a:
    print("less")'''


'''a=10
b=20
if not a>b:
    print("less")'''


'''a=10
b=20
if not a<b:
    print("less")'''


'''a="data science"
if not a=="python":
    print("true")'''


'''a="data science"
if not a!="python":
    print("true")'''


#if condition by using identify operators
#is int,not int 

'''a=10
if type(a) is int:
    print("it is int")'''

'''a=4
if type(a) is not int:
    print("it is int")'''

'''a=int(input())
if type(a) is not int:
    print("true")'''

'''a=int(input())
if type(a) is int:
    print("it is int")'''

#if condition by using membership operators
'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8,9,10
if 15 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8,9,10
if 15 not in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")'''#error

'''a=[1,2,3,4,5,6,7,8,9,10]
b=int(input("a value"))
if b in a:
    print("true")'''

#if-else condition by using comparision operators

'''a=6
b=12
if a<b:
    print("less")
else:
    print("true")'''

'''a=6
b=12
if a==b:
    print("less")
else:
    print("true")'''

'''a=6
b=12
if a<b and b>a:
    print("less")
else:
    print("true")'''

'''a=6
b=12
if a<=b and a>=b:
    print("less")
else:
    print("true")'''

'''a=15
b=12
if a<=b or b>=a:
    print("less")
else:
    print("true")'''

'''a=6
b=12
if a!=b or a==b:
    print("less")
else:
    print("true")'''

'''a=6
b=12
if not a>=b:
    print("less")
else:
    print("true")'''

'''a="python"
if a!="java":
    print("match")
else:
    print("not match")'''


#if-elif-else conditions by using comparision operators

'''a=5
b=7
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''


'''a=5
b=7
if a>b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''


'''a=5
b=8
if a==b and b>a:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''


'''a=7
b=5
if a<b or b>a:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=5
if type(a) is int:
    print("it is int")
elif a:
    print("it is not int")
else:
    print("true")'''


'''a=int(input())
if type(a) is int:
    print("int")
elif type(a) is not int:
    print("not int")
else:
    print("true")'''

    
'''a=input()
if type(a) is int:
    print("int")
elif type(a) is not int:
    print("not int")
else:
    print("true")'''


'''a=1,2,3,4,5,6,7
if 15 in a:
    print("true")
elif 15 not in a:
    print("false")'''

#multiple-if condtions using comparision operators
'''a=6
b=9
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''


'''a=6
b=9
if a>b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=9
b=6
if a<b and a!=b:
    print("less")
if b>a or a<=b:
    print("greater")
if a==b:
    print("equal")
if not a>b:
    print("not")
else:
    print("false")'''

'''a="python"
if type(a) is str:
    print("true")
if type(a) is not str:
    print("false")'''


'''a=13
if type(a) is int:
    print("true")
if type(a) is not int:
    print("false")'''

#nested-if conditions
'''a=2
 b=4
if a<b:
     print("less")
     if b>a:
         print("greater")'''

'''a=12
b=15
if a==b:
     print("less")
     if b>a:
         print("greater")'''

'''a=10
b=5
 if a<b:
     print("less")
     if b==a:
         print("greater")'''

'''a=30
b=40
if a<b:
     print("less")
     if b<a:
         print("greater")
     else:
             print("true")'''


'''a=6
b=12
if a>b:
     print("less")
     if b>a:
         print("greater")
else:
    print("true")'''

'''a=3
b=6
if a==b:
     print("less")
     if b<a:
         print("greater")
     else:
         print("true")
else:
    print("false")'''


'''a=5 
b=10
if a<b:
     print("less")
     if b>a:
         print("greater")
     elif a!=b:
         print("not equal")
     else:
         print("true")'''

#task
#voting
'''a=int(input("age"))
if a>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''


#even or odd
'''a=int(input("num is"))
if a%2==0:
    print("even")
else :
    print("odd")'''


#leap year
'''year = int(input("Enter a year: "))
if year % 4 == 0:
    print("leap year")
else:
    print("Not a leap year")'''

#guest
'''name=input("enter name")
if name=="esali":
    print("welcome",name)
else:
    print("welcome guest")'''
    

'''#5 users
names=["esali","sai","vishnu","priya","aarthi"]
a=input("enter the name")
if a in names:
    print("welcome",a)
else:
    print("welcome guest")'''



#vowels
'''vowels=["a","e","i","o","u"]
a=input("enter letter")
if a in vowels:
    print("it is vowel")
else:
    print("it is consonant")'''



'''vowels=["a","e","i","o","u"]
a=input("enter letter").lower()
if a in vowels:
    print("it is vowel")
else:
    print("it is consonant")'''

   

#if-elif-else
#Bakery
'''a=int(input("enter price"))
if a==1200:
    print("red velvet")
elif a==1000:
    print("choco almond")
elif a==800:
    print("chocolate")
elif a==600:
    print("butterscotch")
else:
    print("cake is not avaliable")'''


#pizza
'''a=input("enter the name")
if a=="bbqpizza":
    print(800)
elif a=="crispychicken":
    print(600)
elif a=="pannerpizza":
    print(400)
elif a=="frenchfries & coke":
    print(250)'''


#multiple-if
'''age=int(input("enter the age"))
marks=int(input("enter the marks"))
attendance=int(input("enter the attendance"))
if age>=18:
    print("eligilbe for vote")
if marks>=80:
    print("eligible for scholorship")
if attendance>=80:
    print("allow to write exam")'''


#using if and else:   
'''age=int(input("enter the age"))
marks=int(input("enter the marks"))
attendance=int(input("enter the attendance"))
if age>=18:
    print("eligilbe for vote")
else:
    print("not eligible for vote")
if marks>=80:
    print("eligible for scholorship")
else:
    print("not eligible for scholorship")
if attendance>=80:
    print("allow to write exam")'''


#nested-if
#social media login
'''username=input("enter username")
password=int(input("enter password"))
if username=="esali":
    if password=="110405":
        print("login sucessful")
    else:
        print("invalid credentials")'''


'''username=input("enter username")
password=int(input("enter password"))
if username=="esali":
    if password=="110405":
        print("login sucessful")
    else:
        print("invalid password")
else:
    print("incorrect username")'''



'''username=input("enter username")
password=int(input("enter password"))
if username=="esali" and password=="110405":
    print("login sucessful")
else:
    print("invalid credentials")'''













         



