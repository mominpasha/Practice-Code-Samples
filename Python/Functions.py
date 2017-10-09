>>> def f();
SyntaxError: invalid syntax
>>> def f():
	print "This is a function"

	
>>> print f()
This is a function
None
>>> def f():
	print "This is a function"
	return 1

>>> print f()
This is a function
1
>>> def sort(arg1,arg2):
	if arg1>arg2:
		returtn arg1,arg2
		
SyntaxError: invalid syntax
>>> def sort(arg1,arg2):
	if arg1>arg2:
		return arg1,arg2
	else:
		return arg2,arg1

	
>>> def sort(arg1,arg2):
	if arg1>=arg2:
		return arg1,arg2
	else:
		return arg2,arg1

	
>>> sort(100,200)
(200, 100)
>>> max,min=sort(100,200)
>>> max
200
>>> min
100
10 20
10 20 30
10 20 30 40
10 20
{'b': 20}
10 20 30
10 20 30 40
>>> 
20
From outside the function 46101932
20
From inside the function 46101932
30
46101812
20
>>> 
[1, 2, 3, 4, 5]
From outside the function 58967144
[1, 2, 3, 4, 5]
From inside the function 58967144
[1, 2, 3, 4, 5, 6]
58967144
[1, 2, 3, 4, 5, 6]
>>> 

[1, 2, 3, 4, 5]
From outside the function 54248552
[1, 2, 3, 4, 5]
From inside the function 54248552
[1, 2, 3, 4, 5, 6]
54248552
[1, 2, 3, 4, 5, 6]
>>> 

[1, 2, 3, 4, 5]
From outside the function 55907432
[1, 2, 3, 4, 5]
{'val': [1, 2, 3, 4, 5]}
From inside the function 55907432
[1, 2, 3, 4, 5, 6]
55907432
[1, 2, 3, 4, 5, 6]
{'f': <function f at 0x0355A2B0>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'XXXXXX_Path/Desktop/test.py', '__package__': None, 'x': [1, 2, 3, 4, 5, 6], '__name__': '__main__', '__doc__': None}
>>> 

[1, 2, 3, 4, 5]
From outside the function 53351528
[1, 2, 3, 4, 5]
{'x': [1, 2, 3, 4, 5]}
From inside the function 53351528

Traceback (most recent call last):
  File "XXXXXX_Path/Desktop/test.py", line 13, in <module>
    f(x)
  File "XXXXXX_Path/Desktop/test.py", line 5, in f
    x =x+10
TypeError: can only concatenate list (not "int") to list
>>> 

10
From outside the function 52393508
10
{'x': 10}
From inside the function 52393508

Traceback (most recent call last):
  File "XXXXXX_Path/Desktop/test.py", line 13, in <module>
    f(x)
  File "XXXXXX_Path/Desktop/test.py", line 6, in f
    val.append(6)
NameError: global name 'val' is not defined
>>> 

10
From outside the function 56587812
10
{'x': 10}
From inside the function 56587812
20
56587692
10
{'f': <function f at 0x040852B0>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'XXXXXX_Path/Desktop/test.py', '__package__': None, 'x': 10, '__name__': '__main__', '__doc__': None}
>>> 

10
From outside the function 45577764
10
{'x': 10}
From inside the function 45577764
20
{'f': <function f at 0x038B52B0>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'XXXXXX_Path/Desktop/test.py', '__package__': None, 'x': 20, '__name__': '__main__', '__doc__': None}
>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

    
>>> # 4 parameters, voltage,state,action,type
>>> # 3 default parameters, 1 non-default parameter
>>> def parrot(voltage, state='a stiff', action='voom', type1='Norwegian Blue'):
    print "-- This parrot wouldn't", action
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type1
    print "-- It's", state, "!"

    
>>> parrot(230)
-- This parrot wouldn't voom
if you put 230 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(230) # 1 positional argument
-- This parrot wouldn't voom
if you put 230 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(230, "A STIFF", "VOOM","INDIGO")# 4 positional arguments
-- This parrot wouldn't VOOM
if you put 230 volts through it.
-- Lovely plumage, the INDIGO
-- It's A STIFF !
>>> parrot(voltage=230,state= "A STIFF",action="VOOM",type1="INDIGO")# 4 keyword arguments
-- This parrot wouldn't VOOM
if you put 230 volts through it.
-- Lovely plumage, the INDIGO
-- It's A STIFF !
>>>  parrot(state= "A STIFF",action="VOOM",voltage=230,type1="INDIGO")# 4 keyword arguments
 
  File "<pyshell#32>", line 2
    parrot(state= "A STIFF",action="VOOM",voltage=230,type1="INDIGO")# 4 keyword arguments
    ^
IndentationError: unexpected indent
>>> parrot(state= "A STIFF",action="VOOM",voltage=230,type1="INDIGO")# 4 keyword arguments
-- This parrot wouldn't VOOM
if you put 230 volts through it.
-- Lovely plumage, the INDIGO
-- It's A STIFF !
>>> parrot()

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    parrot()
TypeError: parrot() takes at least 1 argument (0 given)
>>> parrot(voltage=5,"A STIFF")
SyntaxError: non-keyword arg after keyword arg
>>> parrot("A STIFF",voltage=5)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    parrot("A STIFF",voltage=5)
TypeError: parrot() got multiple values for keyword argument 'voltage'
>>> parrot(100,actor="John")

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    parrot(100,actor="John")
TypeError: parrot() got an unexpected keyword argument 'actor'
>>> def fun(*args):
	print args

	
>>> fun(1)
(1,)
>>> fun(1,2)
(1, 2)
>>> fun(1,2,3)
(1, 2, 3)
>>> fun(1,2,3,4,5,6,7)
(1, 2, 3, 4, 5, 6, 7)
>>> def fun(**kwargs):
	print kwargs

	
>>> fun(num1=1,num2=2,num3=3,num4=4)
{'num4': 4, 'num1': 1, 'num2': 2, 'num3': 3}
>>> fun(num1=[1,2,3])
{'num1': [1, 2, 3]}
>>> def fun(*args):
	print args

	
>>> fun([1,2,3])
([1, 2, 3],)
>>> def fun(**kwargs):
	print kwargs

	
>>> fun([1,2,3,4])

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    fun([1,2,3,4])
TypeError: fun() takes exactly 0 arguments (1 given)
>>> def fun(*pos,**keyword):
	print kwargs

	
>>> def fun(*pos,**keyword):
	print pos,keyword

	
>>> fun([1,2,3,4])
([1, 2, 3, 4],) {}
>>> def fun(*pos,**keyword):
	y=0
	for x in pos:
		y+=x
	return y

>>> fun(1,2,3,4,5)
15
>>> def f():
	print "xyz"
	return 100

>>> a=f()
xyz
>>> a
100
>>> def f():
	print "xyz"
	#return 100

	
>>> a=f()
xyz
>>> a
>>> 


Traceback (most recent call last):
  File "XXXXXX_Path/Desktop/test.py", line 6, in <module>
    f(1,2)
  File "XXXXXX_Path/Desktop/test.py", line 2, in f
    l.append(x)
AttributeError: 'int' object has no attribute 'append'
>>> 

>>> 

[1]
[2]
[1, 3]
>>> 

65455208
[1]
65464000
[2]
65455208
[1, 3]
>>> 

49510032 60933224
[1]
49510020 60931248
[2]
49510008 60933224
[1, 3]
>>> 

<type 'list'>
46757520 57853032
[]
<type 'tuple'>
46757508 46469168
()
<type 'list'>
46757496 57853032
[]
>>> 


Traceback (most recent call last):
  File "XXXXXX_Path/Desktop/test.py", line 9, in <module>
    print f(2,())
  File "XXXXXX_Path/Desktop/test.py", line 3, in f
    print l+(x)
TypeError: can only concatenate tuple (not "int") to tuple
>>> 

(2,)
<type 'tuple'>
10319492 10031152
()
>>> lambda x,y:x*y
<function <lambda> at 0x0343A630>
>>> m=lambda x,y:x*y
>>> m
<function <lambda> at 0x0343A670>
>>> m(10,20)
200
>>> y =lambda x:x%2==0
>>> 
>>> y(10)
True
>>> y(1)
False
>>> def f(f1):
	f1()

	
>>> def f1():
	print "This is function f1"

	
>>> f()

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    f()
TypeError: f() takes exactly 1 argument (0 given)
>>> f(f1)
This is function f1
>>> palin =lambda x:x==x[::-1]
>>> palin("india")
False
>>> palin("malayalam")
True
>>> x="malayalam"
>>> if lambda x:x==x[::-1]==True:
	print "Its a palindrome"

	
Its a palindrome
>>> palin
<function <lambda> at 0x0343A730>
>>> # "anna","civic","level","racecar"
>>> palin("civic")
True
>>> palin("level")
True
>>> list1=["anna","civic","level","racecar"]
>>> map(lambda x:x==x[::-1],list1)
[True, True, True, True]
>>> # use map to find all the even nos in the sequence 1,2,3,4...20
>>> map(lambda x:x%2==0, range(,1,21))
SyntaxError: invalid syntax
>>> map(lambda x:x%2==0, range(1,21))
[False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
>>> filter(lambda x:x%2==0, range(1,21))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> filter(lambda x:x==x[::-1],["anna","civic","level","racecar","cricket","india"])
['anna', 'civic', 'level', 'racecar']
>>> filter(lambda x:x%2!=0, range(1,21))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> list1 = [10,100,2,1,-1,50,43,21]
>>> list1
[10, 100, 2, 1, -1, 50, 43, 21]
>>> min(list1)
-1
>>> red =lambda x,y:x if x<y else y
>>> red(10,20)
10
>>> red(30,100)
30
>>> reduce(red,list1)
-1
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","r:)
	  
SyntaxError: EOL while scanning string literal
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","r")
>>> fo
<open file 'c:\\Users\\srisani\\Desktop\\abc.txt', mode 'r' at 0x03407A70>
>>> fo.read()
'aaaaaaaaaaaa\nbbbbbbbbbbb\nccccccccccccc'
>>> import io
>>> io.DEFAULT_BUFFER_SIZE
8192
>>> fo.seek(0,0)
>>> fo.readline()
'aaaaaaaaaaaa\n'
>>> fo.readline()
'bbbbbbbbbbb\n'
>>> fo.readline()
'ccccccccccccc'
>>> fo.readline()
''
>>> fo.seek(0,0)
>>> fo.readlines()
['aaaaaaaaaaaa\n', 'bbbbbbbbbbb\n', 'ccccccccccccc']
>>> "aaaaa\
bbbbb\
cccc"
'aaaaabbbbbcccc'
>>> # fo.seek(offset, wence)
>>> # wence 0 - absolute file position , 1- relative to current position, 2- relative to end of file
>>> fo.read()
''
>>> len("
KeyboardInterrupt
>>> len("ccccccccccccc")
13
>>> fo.seek(-13,2)
>>> fo.read()
'ccccccccccccc'
>>> len('ccccccccccccc')
13
>>> fo.seek(0,0)
>>> fo.tell()
0L
>>> fo.close()
>>> fo
<closed file 'c:\\Users\\srisani\\Desktop\\abc.txt', mode 'r' at 0x03407A70>
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","r")
>>> fo.read()
'aaaaaaaaaaaa\nbbbbbbbbbbb\nccccccccccccc'
>>> fo.tell()
40L
>>> fo.read()
''
>>> fo.seek(2,0)
>>> fo.tell()
2L
>>> fo.close()
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","w")
>>> fo.write("I am writing into this file. All existing contents will be lost")
>>> fo.close()
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","a")
>>> fo.write("\n I am writing into this file. All existing contents will not be lost")
>>> fo.close()
>>> fo = open(r"XXXXXX_Path \Desktop\abc.txt","r")
>>> fo.tell()
0L
>>> fo.read(5)
'I am '
>>> fo.tell()
5L
>>> fo.tell()
5L
>>> fo.read(10)
'writing in'
>>> fo.tell()
15L
>>> 
