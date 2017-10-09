>>> s = "wipro technologies"
>>> s
'wipro technologies'
>>> s[0]
'w'
>>> type(s)
<type 'str'>
>>> print id(x)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print id(x)
NameError: name 'x' is not defined
>>> print id(s)
52792640
>>> s[0] ="W"

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[0] ="W"
TypeError: 'str' object does not support item assignment
>>> s=s.capitalize()
>>> s
'Wipro technologies'
>>> print id(s)
53019056
>>> s
'Wipro technologies'
>>> s.upper()
'WIPRO TECHNOLOGIES'
>>> list1 =[1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
>>> type(list1)
<type 'list'>
>>> list2=[1,1.0,10000000000000000,1+1j,['a','b','c']]
>>> list2
[1, 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> list2[0]
1
>>> list2[-1]
['a', 'b', 'c']
>>> list2[0:2]
[1, 1.0]
>>> list2[:]
[1, 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> list2[-1]
['a', 'b', 'c']
>>> list2[4]
['a', 'b', 'c']
>>> list2[4][1]
'b'
>>> list2[-1][1]
'b'
>>> list2[-1][-2]
'b'
>>> list2[4]
['a', 'b', 'c']
>>> ['a', 'b', 'c'][1]
'b'
>>> list2[4][1]
'b'
>>> for k in list2:
	print k

	
1
1.0
10000000000000000
(1+1j)
['a', 'b', 'c']
>>> 'c' in list2
False
>>> list2
[1, 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> type('c')
<type 'str'>
>>> 'c' in list2[4]
True
>>> for x in list2[4]:
	print x

	
a
b
c
>>> ['a', 'b', 'c'] in list2
True
>>> list2
[1, 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> print id(list2)
53023448
>>> list2[0]= "List is a mutable object"
>>> list2
['List is a mutable object', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> print id(list2)
53023448
>>> list2
['List is a mutable object', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> list2.append("I am appending this value")
>>> list2
['List is a mutable object', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c'], 'I am appending this value']
>>> list2.insert(0,"Inserting at index '0'")
>>> list2
["Inserting at index '0'", 'List is a mutable object', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c'], 'I am appending this value']
>>> list2.insert(2,"2")
>>> list2
["Inserting at index '0'", 'List is a mutable object', '2', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c'], 'I am appending this value']
>>> list2.append(5)
>>> list2
["Inserting at index '0'", 'List is a mutable object', '2', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c'], 'I am appending this value', 5]
>>> list2.pop()
5
>>> list2.pop()
'I am appending this value'
>>> list2
["Inserting at index '0'", 'List is a mutable object', '2', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> list2.pop(0)
"Inserting at index '0'"
>>> list2
['List is a mutable object', '2', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> del list[1]

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del list[1]
TypeError: 'type' object does not support item deletion
>>> del list2[1]
>>> list2
['List is a mutable object', 1.0, 10000000000000000L, (1+1j), ['a', 'b', 'c']]
>>> del list2
>>> list2

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list2
NameError: name 'list2' is not defined
>>> list3=[1,2,3,4,5]
>>> list3
[1, 2, 3, 4, 5]
>>> return_value =list3.pop()
>>> return_value
5
>>> return_value =del list3[3]
SyntaxError: invalid syntax
>>> list3
[1, 2, 3, 4]
>>> del list3
>>> list3

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list3
NameError: name 'list3' is not defined
>>> list3

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list3
NameError: name 'list3' is not defined
>>> list3=[1,2,3,4]
>>> list3
[1, 2, 3, 4]
>>> del list3[3]
>>> list3
[1, 2, 3]
>>> locals()
{'__builtins__': <module '__builtin__' (built-in)>, 'k': ['a', 'b', 'c'], 'list1': [1, 2, 3, 4, 5], 'list3': [1, 2, 3], '__package__': None, 's': 'Wipro technologies', 'return_value': 5, 'x': 'c', '__name__': '__main__', '__doc__': None}
>>> del list3
>>> locals()
{'__builtins__': <module '__builtin__' (built-in)>, 'k': ['a', 'b', 'c'], 'list1': [1, 2, 3, 4, 5], '__package__': None, 's': 'Wipro technologies', 'return_value': 5, 'x': 'c', '__name__': '__main__', '__doc__': None}
>>> def main():
	a=100
	b=200
	s="String"

	
>>> main.__dict__
{}
>>> def main():
	a=100
	b=200
	s="String"
	print locals()

	
>>> main()
{'a': 100, 's': 'String', 'b': 200}
>>> 
{'a': 100, 'c': 300, 'b': 200}
{'a': 1000, 'c': 3000, 'b': 2000}
>>> list4 =[10,20,'a','b','c']
>>> list4
[10, 20, 'a', 'b', 'c']
>>> list4.sort()
>>> list4
[10, 20, 'a', 'b', 'c']
>>> list4 =['a','b','c',10,20]
>>> list4
['a', 'b', 'c', 10, 20]
>>> list4.sort()
>>> list4
[10, 20, 'a', 'b', 'c']
>>> list4.sort(reverse=True)
>>> list4
['c', 'b', 'a', 20, 10]
>>> list4 =[10,20,'a','b','c']
>>> list4
[10, 20, 'a', 'b', 'c']
>>> list4.sort(reverse=True)
>>> list4
['c', 'b', 'a', 20, 10]
>>> list4 =[10,20,'a','b','c']
>>> sorted(list4)
[10, 20, 'a', 'b', 'c']
>>> sorted(list4,reverse=True)
['c', 'b', 'a', 20, 10]
>>> list4
[10, 20, 'a', 'b', 'c']
>>> list5= ['ccc','aaaa','d','bb']
>>> lsit5

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    lsit5
NameError: name 'lsit5' is not defined
>>> list5
['ccc', 'aaaa', 'd', 'bb']
>>> sorted(list5)
['aaaa', 'bb', 'ccc', 'd']
>>> sorted(list5,reverse=True)
['d', 'ccc', 'bb', 'aaaa']
>>> len("Python")
6
>>> 
>>> len([1,2,3,4,5])
5
>>> sorted_list = sorted(list5)
>>> sorted_list
['aaaa', 'bb', 'ccc', 'd']
>>> list5= ['ccc','aaaa','d','bb']
>>> list5
['ccc', 'aaaa', 'd', 'bb']
>>> len('ccc')
3
>>> len('aaaa')
4
>>> sorted(list5,key=len)
['d', 'bb', 'ccc', 'aaaa']
>>> sorted(list5,key=len,reverse=True)
['aaaa', 'ccc', 'bb', 'd']
>>> len(5)

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
>>> list5= ['ccc','aaaa','d','bb',2,3,4]
>>> sorted(list5,key=len)

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    sorted(list5,key=len)
TypeError: object of type 'int' has no len()
>>> list5= ['ccc','aaa','aaaa','d','b','bb']
>>> list5
['ccc', 'aaa', 'aaaa', 'd', 'b', 'bb']
>>> sorted(list5,key=len)
['d', 'b', 'bb', 'ccc', 'aaa', 'aaaa']
>>> list5= ['cccx','aaaz','dw','bby']
>>> list5
['cccx', 'aaaz', 'dw', 'bby']
>>> def cussort(value):
	return value[-1]

>>> cussort('aaaz')
'z'
>>> cussort('dw')
'w'
>>> # shadow list - 'x','z','w','y'
>>> sorted(list5,key=cusort)

Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    sorted(list5,key=cusort)
NameError: name 'cusort' is not defined
>>> sorted(list5,key=cussort)
['dw', 'cccx', 'bby', 'aaaz']
>>> map(cussort,list5)
['x', 'z', 'w', 'y']
>>> "NameError: name 'cusort' is not defined".split()
['NameError:', 'name', "'cusort'", 'is', 'not', 'defined']
>>> l1=[20,10,'x','r','a','f','c']
>>> sorted(l1,key=cussort)

Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    sorted(l1,key=cussort)
  File "<pyshell#134>", line 2, in cussort
    return value[-1]
TypeError: 'int' object has no attribute '__getitem__'
>>> cussort('x')
'x'
>>> cussort(20)

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    cussort(20)
  File "<pyshell#134>", line 2, in cussort
    return value[-1]
TypeError: 'int' object has no attribute '__getitem__'
>>> sorted(l1)
[10, 20, 'a', 'c', 'f', 'r', 'x']
>>> " ".join(['NameError:', 'name', "'cusort'", 'is', 'not', 'defined'])
"NameError: name 'cusort' is not defined"
>>> ":".join(['11','59','00'])
'11:59:00'
>>> d1 = {}
>>> type(d1)
<type 'dict'>
>>> d1['a']="Alpha"
>>> d1['b']="Beta"
>>> d1['g']="Gamma"
>>> d1
{'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
>>> d1[1]="one"
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> 
>>> d1[[1,2,3]]="list of 1,2 and 3"

Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    d1[[1,2,3]]="list of 1,2 and 3"
TypeError: unhashable type: 'list'
>>> d1[{1:"one"}]

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    d1[{1:"one"}]
TypeError: unhashable type: 'dict'
>>> d1["list"]=[1,2,2,3]
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> d2 = {"a":{"a":1,"b":2}}
>>> d2
{'a': {'a': 1, 'b': 2}}
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> d1['a']
'Alpha'
>>> d1[1]
'one'
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> d1.keys()
['a', 1, 'b', 'list', 'g']
>>> d1.values()
['Alpha', 'one', 'Beta', [1, 2, 2, 3], 'Gamma']
>>> d1.items()
[('a', 'Alpha'), (1, 'one'), ('b', 'Beta'), ('list', [1, 2, 2, 3]), ('g', 'Gamma')]
>>> for akey in d1.keys():
	print akey,"-->",d1[akey]

	
a --> Alpha
1 --> one
b --> Beta
list --> [1, 2, 2, 3]
g --> Gamma
>>> for akey in ['a', 1, 'b', 'list', 'g']:
	print akey,"-->",d1[akey]

	
a --> Alpha
1 --> one
b --> Beta
list --> [1, 2, 2, 3]
g --> Gamma
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> d1['a']
'Alpha'
>>> d1.get('a')
'Alpha'
>>> 'a' in d1
True
>>> 'z' in d1
False
>>> for akey in sorted(['a', 1, 'b', 'list', 'g']):
	print akey,"-->",d1[akey]

	
1 --> one
a --> Alpha
b --> Beta
g --> Gamma
list --> [1, 2, 2, 3]
>>> for akey in sorted(d1.keys()):
	print akey,"-->",d1[akey]

1 --> one
a --> Alpha
b --> Beta
g --> Gamma
list --> [1, 2, 2, 3]

>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'list': [1, 2, 2, 3], 'g': 'Gamma'}
>>> del d1['list']
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> d3 ={1:1,2:1,3:1}
>>> d3
{1: 1, 2: 1, 3: 1}
>>> list5
['cccx', 'aaaz', 'dw', 'bby']
>>> list5[0]
'cccx'
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> d1.keys()
['a', 1, 'b', 'g']
>>> d1['z']

Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    d1['z']
KeyError: 'z'
>>> d1.get('z')
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> 5 in d1
False
>>> 5 in d1.keys()
False
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> d1.get('b')
'Beta'
>>> 'Beta" in d1
SyntaxError: EOL while scanning string literal
>>> 'Beta' in d1
False
>>> 5 in d1.keys()
False
>>> d1
{'a': 'Alpha', 1: 'one', 'b': 'Beta', 'g': 'Gamma'}
>>> d1.keys()
['a', 1, 'b', 'g']
>>> tup1 = (1,2,3)
>>> type(tup1)
<type 'tuple'>
>>> tup2 =("a")
>>> type(tup2)
<type 'str'>
>>> tup2 =("a",)
>>> type(tup2)
<type 'tuple'>
>>> list1

Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list2

Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    list2
NameError: name 'list2' is not defined
>>> list3

Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    list3
NameError: name 'list3' is not defined
>>> list5
['cccx', 'aaaz', 'dw', 'bby']
>>> tuple(list5)
('cccx', 'aaaz', 'dw', 'bby')
>>> tuple("Bangalore")
('B', 'a', 'n', 'g', 'a', 'l', 'o', 'r', 'e')
>>> "Bangalore".split()
['Bangalore']
>>> tup3=tuple(range(1,10))
>>> tup3
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> tup3[0]
1
>>> tup3[-1]
9
>>> tup3[0:2]
(1, 2)
>>> tup3[4:7]
(5, 6, 7)
>>> for ele in tup3:
	print ele

	
1
2
3
4
5
6
7
8
9
>>> 3 in tup3
True
>>> tup3
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> 'a' in tup3
False
>>> tup4 =tuple(range(11,20))
>>> tup3
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> tup4
(11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> tup3+tup4
(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> tup3
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> tup3*3
(1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> list6=['a','b','c']
>>> list6*2
['a', 'b', 'c', 'a', 'b', 'c']
>>> tup3
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> tup3[0]
1
>>> len(tup4)
9
>>> min(tup4)
11
>>> max(tup4)
19
>>> sum(tup4)
135
>>> sorted(tup4,reverse=True)
[19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> tup3+tup4
(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> type(tup3+tup4)
<type 'tuple'>
>>> list1 =[1,2,3,4,5]
>>> list1.append([6,7,8,9])
>>> # list1??
>>> # len(list1)
>>> list1
[1, 2, 3, 4, 5, [6, 7, 8, 9]]
>>> len(list1)
6
>>> list1 =[1,2,3,4,5]
>>> list1.extend([6,7,8,9])
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list1.remove(5)
>>> list1
[1, 2, 3, 4, 6, 7, 8, 9]
>>> list1 =[1,2,3,5,4,5]
>>> list1.remove(5)
>>> list1
[1, 2, 3, 4, 5]
>>> list1.index(3)
2
>>> list6=[1,1,1,1,1,11]
>>> list6
[1, 1, 1, 1, 1, 11]
>>> list6.count(1)
5
>>> list6.reverse()
>>> list6
[11, 1, 1, 1, 1, 1]
>>> list7=[1,2,3,4,True,False,]
>>> list7.sort()
>>> list7
[False, 1, True, 2, 3, 4]
>>> 
