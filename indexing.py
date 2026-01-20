Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[4]
'y'
a[0]
'v'
a[1]
'i'
a[0[+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]=a[9]
    
SyntaxError: '[' was never closed
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
    
'vijayawada'
#this is positive indexing
    

a="i am in delhi"
    
a[3]
    
'm'
a[10]
    
'l'
a[11]
    
'h'
a[0]
    
'i'
>>> a[2]
...     
'a'
>>> a[1]
...     
' '
>>> a[4]
...     
' '
>>> #negative indexing
...     
>>> a="salamma"
...     
>>> a[-1]
...     
'a'
>>> a[5]
...     
'm'
>>> a[0]
...     
's'
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
...     
'ammalas'
>>> a[-7]+[-6]+
...     
SyntaxError: invalid syntax
>>> A[-7]+A[-6]
...     
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    A[-7]+A[-6]
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> a[-5]
...     
'l'
>>> a[-7]+a[-6]
...     
'sa'
