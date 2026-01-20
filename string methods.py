Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#length
a="codegnan"
len(a)
8
a="daniel"
len(a)
6
a="gui"
len(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
a="machine learning"
len(12)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    len(12)
TypeError: object of type 'int' has no len()
len(a)
16
#count
a="twinkle twinkle little star"
a.count(5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(5)
TypeError: count() argument 1 must be str, not int
a.count(t)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.count(t)
NameError: name 't' is not defined
a.count("t")
5
a.count("t")
5
#find a string
a="code"
a[2]
'd'
a="daniel"
a[5]
'l'
b="joseph"
b[4]
'p'
b="new york"
b[5]+b[2]
'ow'
c="c0degnan"
b.find("n")
0
b[5]+b[7]
'ok'
#escape sequences
#\n-new line
#\t-tab space
#n means new line represents\new line
#t means represents tab space \t
#example
a="\name\nmobileno\\tvijaya\\nnokia"
print(a)

ame
mobileno\tvijaya\nnokia
a="name\nmobileno\tmailid\newline
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
a="name:daniel\nmobileno\nuniversity\tmailid"
print(a)
name:daniel
mobileno
university	mailid
#replace
a="i am in school"
a.replace("am")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.replace("am")
TypeError: replace() takes at least 2 positional arguments (1 given)
#replace
a="wait until you succed"
a.replace("wait"",work")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.replace("wait"",work")
TypeError: replace() takes at least 2 positional arguments (1 given)
#upper
a="daniel"
a.upper()
'DANIEL'
a.lower()
'daniel'
b="rakesh"
b.lower()
'rakesh'
a="python"
a.captalize()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a="python"
a.capitalize()
'Python'
b="nandhu"
a.istitle()
False
a="python course"
a.title()
'Python Course'
a="python"
a.startswith(p)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.startswith(p)
NameError: name 'p' is not defined
a="python course"
a.startswith("p")
True
a.endswith("s")
False
a.upper()
'PYTHON COURSE'
a="hello world"
a.isalpha
<built-in method isalpha of str object at 0x0000023D1F96EF70>
a.isalpha()
False
a="helloworld"
a.isalpha()
True
a="hello world"
a.isalnum()
False
#strip
a=" daniel "
a.isdecimal
<built-in method isdecimal of str object at 0x0000023D1F96F870>
a.lstrip()
'daniel '
a.rstrip()
' daniel'
a.strip()
'daniel'
#split
a="i am in london"
>>> a.split()
['i', 'am', 'in', 'london']
>>> b="rahul is good boy"
>>> b.split()
['rahul', 'is', 'good', 'boy']
>>> #join()
>>> a="java python c++"
>>> a.join(a)
'jjava python c++ajava python c++vjava python c++ajava python c++ java python c++pjava python c++yjava python c++tjava python c++hjava python c++ojava python c++njava python c++ java python c++cjava python c+++java python c+++'
>>> a="python",java,c"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="python","java","c"
>>> "".join(a)
'pythonjavac'
>>> " ".join(a)
'python java c'
>>> #concatenation
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> a="code"
>>> b="gnan"
>>> print(a+b)
codegnan
>>> print(a+" "+b)
code gnan
>>> print(a+" "+b)
code gnan
>>> #heading
>>> fname="daniei"
>>> lname"sarah"
SyntaxError: invalid syntax
>>> lname="sarah"
>>> print(fname+lname)
danieisarah
>>> print(fname.title()+" "+lname.title()
Daniei Sarah
>>> print(fname+" "+lname)title()
SyntaxError: invalid syntax
a="4"
a.isalnum(a)
a="