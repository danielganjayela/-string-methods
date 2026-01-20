Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="i am in russia"
>>> pint(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pint(a)
NameError: name 'pint' is not defined. Did you mean: 'print'?
>>> print(a)
i am in russia
>>> a="good boy"
>>> a[::]
'good boy'
>>> a[:2]
'go'
>>> a[::5]
'gb'
>>> a[:4]
'good'
>>> a[-4:]
' boy'
>>> a[::2]
'go o'
>>> a="delhi is capital"
>>> a[::]
'delhi is capital'
>>> a[::4]
'di i'
