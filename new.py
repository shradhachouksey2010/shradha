# s="neeraj"
# print(type(s),type(s.lower))
# print(s.upper)
# print(s.title)
# print(s.capitalize)
# print(s.swapcase)
# s="this is python class"
# print(s.index('P'))
# print(s.index('p'))
# print(s.replace('s','xyz'))
# s.capitalize
# print(s.startswith('this'))
# print(s.endswith('ss'))
# s1='python'
# s2='java' 
# s3='php'
# s='seperated_by'.join([s1,s2,s3])
# print(' '.join([s1,s2,s3]))
# print(' '.join(s1,s2,s3))
# print(' '.join((s1,s2,s3)))
# print(s.split(' '))
# print(s.split(''))
# print(s.split(' ',0))
# print(s.split('s'))
# print(l.index('10'))
# l1=[10,20,30,40]
# l1.pop(1)
# print(l1 .pop())
# l=[10,20,30,'python']
# l.remove(10)
# print(l)
# l=[1,2,3,4,'python']
# l.sort()
# l=['python','java','php']
# l.sort()
# print(l)
# print(id(l))
# l=['python','java','php']
# l.reversec()
# print(l)
# l=['python','java','php']
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l1=[1,2,3,4,5,10,2,3]
# print(l.count(10))
# print(l.count(3))
# d={'name':'neeraj','age':37,'qualifization':'m.tech'}
# print(d)
# type(type(d))
# id(id(d))
# max(max(d))
# min(min(d))
# sum(sum(d))
# d={1:1,2:2,3:3}
# print(d)
# # sum(sum(d))
# d1={1:'neeraj',2:37,'quali':2009}
# print(d1)
# d2={'name':'shradha','age':16,'qualifization':'th'}
# d2=d.copy()
# print(d)
# print(d2)
# print(id(d),id(d2))
# d={'name':'shradha','age':16,'qualifization':'th'}
# # d=d.clear()
# # print(d)
# n=d.get('name')
# print(n)
# n=d.get('name','guest')
# print(n)
# print(d.items())
# print(d.keys())
# print(d.values())
# x=d.pop('name')
# print(x)
# print(d)
# x=d.popitem()
# print(x)
# print(d)
# d1={'x':10,'y':20,'z':30}
# d.update(d1)
# print(d)
# print(d1)
# s='python'
# d=dict.fromkeys(s)
# d=dict.fromkeys(s,100)
# print(d)
# d.setdefault('name','shradha')
# print(d)
# d.setdefault('p',10)
# print(d)
# my_set={10,20,30,'python','java'}
# print(my_set)
# print(type(my_set))
# print(id(my_set))
# print(len(my_set))
# print(max(my_set))
# print(min(my_set))
# print(sum(my_set))
# s={10,20,30,'python','java'}
# s.add('php')
# print(s)
# s.update(['xyz','abc'])
# print(s)
# s.update('python')
# print(s)
# s.remove('python')
# print(s)
# s.discard('python')
# print(s)
# s.discard('java')
# print(s)
# s.remove('java')
# print(s)
# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.intersection_update (s2))
# print(s1)
# print(s2)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s1.difference_update(s2))
# print(s1)
# print(s2)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s1.symmetric_difference_update(s2))
# print(s1)
# print(s2)

# s1={1,2,3,4,5,6,7,8,9,10,11,12}
# s2={5,6,9,10}
# print(s1.issubset(s2))
# print(s2.issubset(s2))
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s1))


# LOOP

# for i in "python":
#     print(i)
# for i in [10,20,30,40]:
#     print(i)    
# for i in range(4):
#     print("hello")
# for i in range(1,11):
#     print(i)    
# for i in "python":
#     print(i,end=(','))
# for _ in range(4):
#     print("hello") 
    
# d={"name":"shradha","age":"16","city":"mandideep"}
# for i in d:
#     print(i) 
# for i in d:
#     print(i,"=",d.get(i)) 
# O/P:-
# name
# age
# city
# name = shradha
# age = 16
# city = mandideep

# n=7
# i=1
# while i<=n:
#     if i<n:
#       print(i,end='+') 
#     else:
#       print(i)
#     i=i+1
# O/P:-
# 1+2+3+4+5+6+7

# n=7
# i=1
# while i<=n:
#     if i<n:
#       print(i,end='+') 
#     else:
#       print(i,end='=')
#     i=i+1
# O/P:-
# 1+2+3+4+5+6+7=

# n=7
# i,sum=1,0
# while i<=n:
#    #  sum=sum+i
#     if i%2==0<n:
#       print(i,end=',') 
#     else:
#       print(i)
#       # print(sum)
#     i=i+1
# O/P:-
# 1
# 2,3
# 4,5
# 6,7

# n=10
# for i in (range(n)):
#     print ('*'*n)
# o/p:-
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

# n=5
# for i in range(1,n+1):
#     print('*'*i+' '*(n-1))
#     # print(' '*(n-i)+'*'*i)
# o/p:-
# *    
# **    
# ***    
# ****    
# ***** 

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)
# O/P:-
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# n=5
# for i in range (n):
#     print('*'*(n-i)+' '*i)       
# O/P:-
# *****
# **** 
# ***  
# **   
# *  

# n=5
# for i in range(n):
#     print(' '*i+'*'*(n-i))
# O/P:-
# *****
#  ****
#   ***
#    **
#     *

# n=5
# for i in range(n):
#     print(' '*i+'* '*(n-i))
# O/P:-
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# n=5
# for i in range(1,n+1):
#     print('*'*i+' '*(n-i))
# for i in range(n):
#     print('*'*(n-i)+' '*i)
# o/p:-
# *    
# **   
# ***  
# **** 
# *****
# *****
# **** 
# ***  
# **   
# * 

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i) 
# for i in range(1,n-1):
#     print(' '*i+'*'*(n-i))
# o/p:-
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)
# for i in range(1,n-1):
#     print(' '*i+'* '*(n-i))
# o/p:-
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

# n=5
# for i in range(1,n+1):
#     print('*'*i+' '*(n-i))
# # print(i)
# i=i-1    
# for i in range(4,0,-1):
#     print('*'*i+' '*(n-i))
# o/p:-
# *    
# **   
# ***  
# **** 
# *****
# **** 
# ***  
# **   
# *  

# n=5
# for i in range(0,n):
#     print('*'*(n-i)+' '*i)
# for i in range(3,-1,-1):
#     print('*'*(n-i)+' '*i)
# o/p:-
# *****
# **** 
# ***  
# **   
# *    
# **   
# ***  
# **** 
# *****

# n=5
# for i in range(0,n):
#     print('*'*(n-i)+' '*i)
# for i in range(2,n+1):
#     print('*'*i+' '*(n-i))
# o/p:-
# *****
# **** 
# ***  
# **   
# *    
# **   
# ***  
# **** 
# *****

# n=6
# for _ in range(n):
#     for i in range(1,n+1):
#         print(i,end =' ')
#     print()
# o/p:-
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 
    
# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end =' ')
#     print()
# o/p:-
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()     
# o/p:-
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        print(2*j,end=' ')
#     print()    
# o/p:-
# 2 
# 2 4 
# 2 4 6 
# 2 4 6 8 
# 2 4 6 8 10 
 
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        print(2*j-1,end=' ')
#     print()  
# o/p:- 
# 1 
# 1 3 
# 1 3 5 
# 1 3 5 7 
# 1 3 5 7 9 

# n=5
# x=1
# for i in range(1,n+1):
#     for i in range(1,i+1):
#         print(2*x,end=' ')
#         x=x+1
#     print()
# o/p:-
# 2 
# 4 6 
# 8 10 12 
# 14 16 18 20 
# 22 24 26 28 30 

# n=5
# for i in range(1,n+1):
#     x=1
#     for i in range(1,i+1):
#         print(2*x,end=' ')
#         x=x+1
#     print()
# o/p:-
# 2 
# 2 4 
# 2 4 6 
# 2 4 6 8 
# 2 4 6 8 10 

# n=5
# x=1
# for i in range(1,n+1):
#     for i in range(1,i+1):
#         print(2*x-1,end=' ')
#         x=x+1
#     print()
# o/p:-
# 1 
# 3 5 
# 7 9 11 
# 13 15 17 19 
# 21 23 25 27 29 

# ch=input("enter any charactor:")
# print(chr(ord(ch)+1))
# o/p:-
# b

# n=5
# ch='a'
# for i in range(n):
#     print(ch,end=' ')
#     ch=chr(ord(ch)+1)
# o/p:-
# a b c d e 

# n=5
# ch='a'
# for i in range(1,n+1):
#     for _ in range(n):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()
# o/p:-
# a b c d e 
# f g h i j 
# k l m n o 
# p q r s t 
# u v w x y 

# n=5
# for i in range(1,n+1):
#     ch='a'
#     for _ in range(n):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()
# o/p:-
# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 

# n=5
# for i in range(1,n+1):
#     ch='a'
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()
# o/p:-
# a 
# a b 
# a b c 
# a b c d 
# a b c d e 

# n=5
# ch='a'
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#     print()
# o/p:-
# a 
# b c 
# d e f 
# g h i j 
# k l m n o 

# n=5
# ch='a'
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)+2)
#     print()
#  o/p:-
# a 
# c e 
# g i k 
# m o q s 
# u w y { } 

# n=5
# ch='A'
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)-1)
#     print()
# o/p:-
# A 
# @ ? 
# > = < 
# ; : 9 8 
# 7 6 5 4 3 

# n=5
# ch='a'
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=' ')
#         ch=chr(ord(ch)-1)
#     print()
# o/p:-
# a 
# ` _ 
# ^ ] \ 
# [ Z Y X 
# W V U T S
# 


# while loop #


# n=12345
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)
# o/p:-
# 5

# n=(int(input("enter any numder:")))
# x=n
# rev=0
# while  n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# # print(rev)
# if x==rev:
#     print(f'given number {x}is palindrom')
# else:
#     print(f'given number{x}is not palidrom')

# n=(int(input("enter any number:")))
# count=sum=0
# x=y=n
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# while x>0:
#     ld=x%10
#     sum=sum+ld**count
#     x=x//10
# if y==sum:
#     print("armstrong")
# else:
#     print("nota armstrong")


# s=input("enter any string")
# s1=' '
# for i in s:
#     s1=i+s1
# if s==s1:
#     print("palindrom")
# else:
#     print("not a palindrom")


# n=input("enter any string")
# vol=con=0
# for i in n:
#     if 65<=ord(i)<=90 or 97<=ord(i)<=122:
#         if i in ['a','e','i','0','u','A','E','I','O','U']:
#             vol=vol+1
#         else:
#             con=con+1
#     else:
#         pass
# print(f'total vovel count is{vol}')
# print(f'total con count is{con}')
#              (Or)
# n=(input("enter any string"))
# vol=con=0
# for i in n:
#     if 65<=ord(i)<=90 or 97<=ord(i)<=122:
#         if i.lower() in ['a','e','i','0','u']:
#             vol=vol+1
#         else:
#             con=con+1
# print(f'total vovel count is{vol}')
# print(f'total con count is{con}')
# o/p:-
# enter any string shradha
# total vovel count is2
# total con count is5


# n=input("enter any str")
# vov=con=0
# for i in n:
#     if 97<=ord(i.lower())<=122:
#         if i.lower()in ['a','e','i','o','u']:
#             vov=vov+1
#         else:
#             con=con+1
# print(f'total vovel count is{vov}')
# print(f'total con count is{con}')
# o/p:-
# enter any string shradha
# total vovel count is2
# total con count is5


# n=int(input('enter any no'))
# i=1
# while i<=n:
#     if i==5:
#         continue
#     print(i)
#     i=i+1
# o/p:-
# enter any no 5
# 1
# 2
# 3
# 4


# n=int(input('enter any no'))
# i=1
# while i<=n:
#     if i==5:
#        pass
#     else:
#        print(i)
#     i=i+1
# o/p:-
# enter any no 10
# 1


# n=int(input('enter any no'))
# i=1
# while i<=n:
#     if i==5:
#        i=i+1
#        continue
#     print(i)
#     i=i+1
# o/p:-
# enter any no 10
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# n=int(input('enter any no'))
# i=1
# while i<=n:
#     if i==5:
#        print("xyz")
#        break
#     print(i)
#     i=i+1
# print("hello")
# 0/p:-
# enter any no 5
# 1
# 2
# 3
# 4
# xyz
# hello


# while True:
#     print("hello")

# while True:
#     print("1.add(+)\n2.sub(-)\n3.multi(*)\n4.div\n5.exit")
#     n=int(input("enter any above option:"))
# o/p:-
# 1.add(+)
# 2.sub(-)
# 3.multi(*)
# 4.div
# 5.exit


# while True:
#     print("1.add(+)\n2.sub(-)\n3.multi(*)\n4.div\n5.exit")
#     n=int(input("enter any above option:"))
#     if n in [1,2,3,4]:
#         pass
#     elif n==5:
#         break
#     else:
#         print('please enter valid optin')
# o/p:-
# 1.add(+)
# 2.sub(-)
# 3.multi(*)
# 4.div
# 5.exit
# enter any above option:1
# please enter valid optin
# 1.add(+)
# 2.sub(-)
# 3.multi(*)
# 4.div
# 5.exit
# enter any above option:3


# while True:
#     print("1.add(+)\n2.sub(-)\n3.multi(*)\n4.div\n5.exit")
#     n=int(input("enter any above option:"))
#     if n in [1,2,3,4]:
#         if n==1:
#             x=int(input("pls enter how many numbers you want to add"))
#             l=[]
#             for i in range(1,x+1):
#                 num=int(input(f'piease enter {i}number:'))
#                 l.append(num)
#             print(f'addition of given numbers{l}={sum(l)}')
#     elif n==5:
#         break
#     else:
#         print('please enter valid optin')
# o/p:-
# 1.add(+)
# 2.sub(-)
# 3.multi(*)
# 4.div
# 5.exit
# enter any above option:1
# pls enter how many numbers you want to add6
# piease enter 1number:40
# piease enter 2number:40
# piease enter 3number:38
# piease enter 4number:12
# piease enter 5number:90
# piease enter 6number:10
# addition of given numbers[40, 40, 38, 12, 90, 10]=230


# def hello():
#     print("hello")
#     return
# hello()
# x= hello()
# print(x)
# print(x)
# print(x)
# print(hello())
# o/p:-
# hello
# None
# None
# None
# hello
# None


# x=10
# print(x)
# print(print(x))
# o/p:-
# 10
# None


# positional argument

# def add(x,y):
#     return x+y
# p=int(input("enter any no:"))
# q=int(input("enter any no:"))
# result=add(p,q)
# print(result)
# o/p:-
# w.py
# enter any no:10
# enter any no:20
# 30


# def add(x,y):
#     return x+y
# p=int(input("enter any no:"))
# q=int(input("enter any no:"))
# result=add(p)
# print(result)
# o/p:-
# error


# def add(x,y):
#     return x+y
# p=int(input("enter any no:"))
# q=int(input("enter any no:"))
# r=int(input("enter any no:"))
# result=add(p,q,r)
# print(result)
# o/p:-
# TypeError: add() takes 2 positional arguments but 3 were given


# default positional argument

# def add(x=0,y=0):
#     return x+y
# print (add())
# o/p:-
# 0


# def add(x=0,y=0):
#     return x+y
# print(add(10))
# 0/p:-
# 10


# def add(x=0,y=0):
#     return x+y
# print(add(10,20))
# o/p:-
# 30


# def add(x=0,y=0):
#     return x+y
# print(add(10,20,30,40,50))
# o/p:-
# TypeError: add() takes from 0 to 2 positional arguments but 5 were given


# def add(* args):
#     print(args)
#     print(type(args))
# add()
# add(10)
# add(10,20,30,40)
# o/p:-
# ()
# <class 'tuple'>
# (10,)
# <class 'tuple'>
# (10, 20, 30, 40)
# <class 'tuple'>


# x=10
# x1=(10)
# x2=10,
# x3=(10,)
# print(type(x3))


# def add (*n):
#     print(n)
#     print(type(n))
# add (10,20,30,40)
# o/p:-
# (10, 20, 30, 40)
# <class 'tuple'>


# def add(*n):
#     res=sum(n)
#     return res
# result=add(10,20,30,40)
# print(result)
# o/p:-
# 100


# s=(10,20,30,40,50)
# sum=0
# for i in s:
#     sum =sum+i
#     print(sum)
# o/p:-
# 10
# 30
# 60
# 100
# 150


# def add (*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum 
# result= add (10,20,30,40)
# print(result)
# o/p:-
# 100


# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# x=eval(input("enter any value:"))
# result=add(*x)
# print(result)
# o/p:-
# 100








# i=1
# for i in range(1,11):
#     print(f"2*{i}={i*2}")
# o/p:-
# 2*1=2
# 2*2=4
# 2*3=6
# 2*4=8
# 2*5=10
# 2*6=12
# 2*7=14
# 2*8=16
# 2*9=18
# 2*10=20


# variable scope

# local

# def add():
#     x=10
#     y=20
#     print(x+4)
#     print(x)
# add()
# # print(x)


# x=10
# y=20
# def add():
#     print(x+4)
# add()
# print(x,4)


# x=10
# def display():
#     print(x)
#     x=20
#     print(x)
# display( )
# o/p:-
# error


# x=10
# def display():
#     x=20
#     print(x)
# display( )
# print(x)
# 0/p:-
# 20
# 10

# global

# x=10
# def display():
#     global x
#     x=20
#     print(x)
# print(x)
# display()
# print(x)
# o/p:-
# 10
# 20
# 20


# x=10
# def display():
#     x=20
#     print(x)
#     print(globals ()['x'])
# display()
# o/p:-
# 20
# 10


# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         print(x)
#         x=20
#         return x
#     res=inner()
#     return res 
# res=outer()
# print(res)
# o/p:-
# 10
# 20


# def outer():
#     x=10
#     def inner():
#         print(x)
#         x=20
#         return x
#     res=inner()
#     return res 
# res=outer()
# print(res)
# o/p:-
# Error
# print(x)


