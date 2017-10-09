>>> set1 =set()
>>> type(set1)
<type 'set'>
>>> set2={}
>>> type(set2)
<type 'dict'>
>>> set2={3,4,5}
>>> type(set2)
<type 'set'>
>>> tup1=(1,2,3,4,5)
>>> dic = {1:'a',2:'b'}
>>> dic[1]
'a'
>>> list1=[]
>>> list1
[]
>>> tupe=()
>>> dic1={}
>>> tup1
(1, 2, 3, 4, 5)
>>> set3=set(tup1)
>>> set3
set([1, 2, 3, 4, 5])
>>> lis1=[1,2,3,4,5,6]
>>> set4 =set(lis1)
>>> set4
set([1, 2, 3, 4, 5, 6])
>>> len(set3)
5
>>> set1
set([])
>>> list3=[]
>>> list3
[]
>>> "string"
'string'
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> (1,2,3,44)
(1, 2, 3, 44)
>>> {1:2,2:2}
{1: 2, 2: 2}
>>> {1,2,3,4}
set([1, 2, 3, 4])
>>> set5 = set("abcd")
>>> set5
set(['a', 'c', 'b', 'd'])
>>> set1
set([])
>>> set2
set([3, 4, 5])
>>> for x in set2:
	print x

	
3
4
5
>>> set2.add("hello")
>>> set2
set([3, 4, 5, 'hello'])
>>> set2.remove(5)
>>> set2
set([3, 4, 'hello'])
>>> dir(set2)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set2
set([3, 4, 'hello'])
>>> set2.pop()
3
>>> set2.pop()
4
>>> tuple("abcd")
('a', 'b', 'c', 'd')
>>> list("abcd")
['a', 'b', 'c', 'd']
>>> set("abcd")
set(['a', 'c', 'b', 'd'])
>>> s={1,2,3,4,5,5,6,7,8,9}
>>> s
set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> type(s)
<type 'set'>
>>> len(s)
9
>>> min(s)
1
>>> max(s)
9
>>> sum(s)
45
>>> s.add("1")
>>> s
set([1, 2, 3, 4, 5, 6, 7, 8, 9, '1'])
>>> sum(s)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sum(s)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> s
set([1, 2, 3, 4, 5, 6, 7, 8, 9, '1'])
>>> s.add(1)
>>> s
set([1, 2, 3, 4, 5, 6, 7, 8, 9, '1'])
>>> s
set([1, 2, 3, 4, 5, 6, 7, 8, 9, '1'])
>>> s.pop(5)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.pop(5)
TypeError: pop() takes no arguments (1 given)
>>> s1=set(range(1,60))
>>> s1
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
>>> s1=set(range(1,6))
>>> s1
set([1, 2, 3, 4, 5])
>>> s2=set(range(1,11))
>>> s2
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> s1.issubset(s2)
True
>>> s2.issuperset(s1)
True
>>> s1<s2
True
>>> s2>s1
True
>>> s1.issubset(s1)
True
>>> s1<s1
False
>>> s1<=s1
True
>>> s1>=s1
True
>>> s3={1,2,3}
>>> s4={1,2,3}
>>> s3<s4
False
>>> s3<=s4
True
>>> s1
set([1, 2, 3, 4, 5])
>>> s2
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> s2=set("wipro")
>>> s2
set(['i', 'p', 'r', 'o', 'w'])
>>> s1
set([1, 2, 3, 4, 5])
>>> s1.union(S2)

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s1.union(S2)
NameError: name 'S2' is not defined
>>> s1.union(s2)
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> s1.intersection(s2)
set([])
>>> s1|s2
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> s1&s2
set([])
>>> s1.difference(s2)
set([1, 2, 3, 4, 5])
>>> s1-s2
set([1, 2, 3, 4, 5])
>>> s2-s1
set(['i', 'p', 'r', 'w', 'o'])
>>> s1.symmetric_difference(s2)
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> s2^s1
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> s1^s2
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> s2^s1
set([1, 2, 3, 4, 5, 'i', 'o', 'p', 'r', 'w'])
>>> #s1-s2!=s2-s1
>>> #s1^s2==s2^s1
>>> s5={1,2,3,4}
>>> s6={2,3,4,5}
>>> s5^s6
set([1, 5])
>>> s6^s5
set([1, 5])
>>> s7={1,3,4}
>>> type(s7)
<type 'set'>
>>> s8 ={[1,2],[3,4]}

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s8 ={[1,2],[3,4]}
TypeError: unhashable type: 'list'
>>> s9={(1,2,3),(3,2,1)}
>>> s9
set([(3, 2, 1), (1, 2, 3)])
>>> s10={(1,2,[2,3]),(4,5)}

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s10={(1,2,[2,3]),(4,5)}
TypeError: unhashable type: 'list'
>>> s11 = {{1,2},{3,4}}

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    s11 = {{1,2},{3,4}}
TypeError: unhashable type: 'set'
>>> x=100
>>> if x==100:
	print x

	
100
>>> if x==200:
	print x
else:
	print x+x

	
200
>>> if x==200:
	print x
else:
	print x+x

	
200
>>> x
100
>>> 
Enter the marks77
B grade
>>> 
================= RESTART: C:/Users/srisani/Desktop/test.py =================
Enter the marks80
B grade
>>> x

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=10
>>> y=1 if x>0 else -1
>>> y
1
>>> y="Even" if x%2==0 else "odd"
>>> y
'Even'
>>> y="Even" if x%2==0 and if x<=10 else "odd"
SyntaxError: invalid syntax
>>> if(x<5) y=1 elseif(x<10) y=2 else if(x<20) y=3
SyntaxError: invalid syntax
>>> y="Even" if x%2==0 and x<=10 else "odd"
>>> y
'Even'
>>> # range(start_value,end_value+1,step_size)
>>> range(0,10,1)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(0,10,2)
[0, 2, 4, 6, 8]
>>> list1=[]
>>> for x in range(1,10):
	list1.append(x**2)

	
>>> list1
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list1=[]
>>> for x in range(0,10):
	list1.append(x**2)

	
>>> list1
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> l1=[x*x for x in range(10)]
>>> l1
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> l1=[x*x for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
>>> l1
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [2*x for x in range(13)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
>>> [2**x for x in range(13)]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
>>> l1= [2**x for x in range(12)]
>>> l1
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
>>> S=[x**2 for x in range(0,10)]
>>> S
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x for x in S if x%2==0]
[0, 4, 16, 36, 64]
>>> [x**2 for x in range[0,9,2]]

Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    [x**2 for x in range[0,9,2]]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> [x**2 for x in range(0,9,2)]
[0, 4, 16, 36, 64]
>>> words = "The quick brown fox jumps over the lazy dog"
>>> words
'The quick brown fox jumps over the lazy dog'
>>> [[word.upper(),word.lower(),len(word)]for word in words]
[['T', 't', 1], ['H', 'h', 1], ['E', 'e', 1], [' ', ' ', 1], ['Q', 'q', 1], ['U', 'u', 1], ['I', 'i', 1], ['C', 'c', 1], ['K', 'k', 1], [' ', ' ', 1], ['B', 'b', 1], ['R', 'r', 1], ['O', 'o', 1], ['W', 'w', 1], ['N', 'n', 1], [' ', ' ', 1], ['F', 'f', 1], ['O', 'o', 1], ['X', 'x', 1], [' ', ' ', 1], ['J', 'j', 1], ['U', 'u', 1], ['M', 'm', 1], ['P', 'p', 1], ['S', 's', 1], [' ', ' ', 1], ['O', 'o', 1], ['V', 'v', 1], ['E', 'e', 1], ['R', 'r', 1], [' ', ' ', 1], ['T', 't', 1], ['H', 'h', 1], ['E', 'e', 1], [' ', ' ', 1], ['L', 'l', 1], ['A', 'a', 1], ['Z', 'z', 1], ['Y', 'y', 1], [' ', ' ', 1], ['D', 'd', 1], ['O', 'o', 1], ['G', 'g', 1]]
>>> [[word.upper(),word.lower(),len(word)]for word in words.split()]
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
>>> 
