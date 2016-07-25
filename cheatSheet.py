
'----------------------------------------------------------------------------------------------------'

# strings, quotations, escaping

'spam eggs'				# single quotes
'doesn\'t'				# use \' to escape the single quote...
"doesn't"				# ...or use double quotes instead

3*'un' + 'ium'				# n*str gives str repeated n times

'Py' 'thon'			    	# str literals concatenated, 
					# useful for breaking long strings into multiple lines

word = 'Python'
word[0]					# P
word[-1]				# n - 1st from the end

word[0:2]				# slice, first included, second excluded
word[:2] + word[2:]			# from beginning to 2nd and from 2nd to the end
word[:]					# the whole word

# strings are immutable, you have to compile new one

len(word)				# built in function for string lenth

str(3)					# convert to string
str(3).zfill(2)                         # 03

'----------------------------------------------------------------------------------------------------'

# lists

squares = [1, 4, 9, 16, 25]
squares[0]				# 1
squares[-1]				# 25 
squares[-3:]				# 9, 16, 25 
squares[:]				# full list, the easyest way to copy it
squares + [36, 49, 64, 81, 100]

# lists are mutable
cubes = [1, 9, 27, 65, 125]
cubes[3] = 4 ** 3			# ** has higher priority than -, -3**2 = -9

cubes.append(216)

# assignment to slises is possible

letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters[2:5] = ['C', 'D', 'E']		# ['a', 'b', 'C', 'D', 'E', 'f']
letters[2:5] = []			# ['a', 'b', 'f']
letters[:] = []				# []

len(letters)				# bultin length function

nested = [1, [2, 3]]
nested[1][1]				# 3

'----------------------------------------------------------------------------------------------------'

# swapping variable values
a, b = 0, 1
a, b = b, a
a, b = b, a				# 0, 1 again

'----------------------------------------------------------------------------------------------------'

while b < 10:				# 
    print(b)
    a, b = b, a + b			# body indented, this hows it's integrity
					# right-hand side is evaluated firs, from left to right

'----------------------------------------------------------------------------------------------------'

i = 256 ** 2
print('asdf')				# prints the argument
print('asdf', i)			# asdf 65536	     note the space after asdf

print('asd1', end=',')			# will replace default (eol) end simbol with specified
print('asd2', end=',')			# asd1,asd2,

'----------------------------------------------------------------------------------------------------'

			# in conditions
			# non zero integer is true, zero is false
			# non empty sequence (string, list, etc.) is true, empty is false

'----------------------------------------------------------------------------------------------------'



####    4   Control flow

'----------------------------------------------------------------------------------------------------'

x = int(input("Please enter number: "))	#	- invite to enter integer

'----------------------------------------------------------------------------------------------------'

if 0==0:
	smth
elif 1==1:
	smth
elif 2==2:
	smth
else:
	smth

'----------------------------------------------------------------------------------------------------'

range(5)				# 0 1 2 3 4		end
range(1, 10)				# 1 2 3 4 5 6 7 8 9	start end
range(1, 10, 3)				# 1 4 7			start end step

print(range(5))				# range(0, 5)
list(range(5))				# [0, 1, 2, 3, 4]

'----------------------------------------------------------------------------------------------------'

words = ['123456', '12345', '1234']

for w in words:                         # enumerating by items
	print(w, len(w))

for i in range(len(words))              # enumerating by indexes
	print(i, words[i])
        
for w in words[:]:                      # enumerating by items in the copy
    if(len(w) < 4)
        break                           # terminates loop execution
    if(len(w) < 5)
        continue                        # terminates current ittereation, skips to the next one
    words.insert(0, w)
else:                                   # executes if loop is finished and break wasn't called
    print('all words of length greater than 5 was duplicated')

'----------------------------------------------------------------------------------------------------'

pass                                    # does nothing, used for empty classes and functions

'----------------------------------------------------------------------------------------------------'

# functions

def printingFunction(parameter):
    """this is function description, always use this"""
    print(parameter)

def add(a, b):
    """adding function"""
    return a + b 

printingFunction('something to print')

p = printingFunction                    # variable p now is equal to function printingFunction

print('printing result', p('asdf'))     # function without a return statement returns None 
                                        # return statement without parameter also returns None

# default argument values

def increment(a, b = 1):
    """increments first argument by some value, by default 1"""
    return a+b

print(increment(10))
print(increment(10, 2))

			# variable value may be used for default value
			# value that is actual at the time of 
			# function difinition will be used

			# if def value is mutable, 
			# mutations will be preserved from call to call
def a(a, L=[]):
    L.append(a)
    return L

a(1)                                    # [1]
a(2)                                    # [1, 2]
a(3,[])                                 # [3]
a(4)                                    # [1, 2, 4]

def a(a, L=None):                       # this is the trick for preventing this 
    if L is None: 
        L=[]
    L.append(a)
    return L


# keyword arguments

def addingManyValues(a, b=1, c=2):
    return a + b + c

addingManyValues(1)
addingManyValues(1, b=3)
addingManyValues(1, c=4)
addingManyValues(1, c=4, b=3)

					# you can't:
addingManyValues(b=3, 1)		# pass positional argument after keyword one
addingManyValues(1, a=7)		# pass parameter value multiple times
addingManyValues(b=3)	                # skip argument without a default value
addingManyValues(1, lord='marshal')	# pass anknown keyword paramenter


# arbitrary number of positional and keyword arguments 

def allTheArgs(a, *arguments, **dictionary, b=1):
    print(a, b)
    for arg in arguments:		# *name arg will get all the positional arguments beyond a
	print(arg)
    keys = sorted(dictionary.keys())	# **name arg will get dict of all the keyword args beyond b
    for key in keys:			
	print(key, ': ', dictionary[key])

allTheArgs(a, 4, 2, 3, lord='marshal', b=2)


# unpacking arguments, reverse situation

args = [1, 2]
add(*args)				# * in front of sequence unpacks it into positioned args

args = {'a':1, 'b':2, 'c':3}
addingManyValues(**args)		# ** unpacks dictionary into keyworded args 


# lambda expression

addLambda = lambda a, b: a+b		# created function adding together it's two args
addLambda(1, 2)				# 3

def functionAddingNumber(a):
    return lambda x: x + a		# generates a new function that will add a to it's argument

addFortyTwo = functionAddingNumber(42)	# function adding 42 to it's argument

addFortyTwo(0)				# 42
addFortyTwo(1)				# 43

					# useful for passing function as an argument

pairs = [(1, b), (2, f), (3, a)]
paris.sort(key=lambda pair: pair[1])
pairs					# [(3, a), (1, b), (2, f)]


# doc string

					# first line is short summary 
					# without mentioning function name or type
					# starts with capital, ends with period

def docFunc():
    """Does nothing, but documents it.

    No more descriptions here.		
    """
    pass
					# if there's more than one line, second one should be blank
					

# function annotation

def increments(a: int, b:int = 1) -> int:
    return a + b

increments.__annotations__		#{'renurn': <class 'int'>, 'a': <class 'int'>, 
					#   'b': <class 'int'>}
					# without type annotations it would return {}

'----------------------------------------------------------------------------------------------------'



####    5   data structures

'----------------------------------------------------------------------------------------------------'


# 5.1 list

x=42
L=[] 
i=0
list = []

list.append(x)                          # appends item to the end
list.extend(L)                          # appends L list items to the end
list.insert(i, x)                       # inserts x item at position i
list.remove(x)                          # removes first occurance of x
list.pop([i])                           # removes and returns item at position i, () removes last one
list.clear()                            # remove all items. Equiv. to del a[:]
list.index(x)                           # returns index of first x in the list, error if not found
list.count(x)                           # returns number of items
list.sort(key=None, reverse=False)      # sorts the list
list.reverse()                          # reverses the items order
list.copy()                             # return a shallow copy. Equiv. to a[:]


# 5.1.1 using list as a stack, this is efficient

list.append(42)
list.pop()                              # 42


# 5.1.2 using list as a queue is not efficient, use deque instead
                                        
from collections import deque           # collections.deque, append and pop is fast from both ends
queue = deque(['a', 'b', 'c'])
queue.append('d')
queue.popleft()                         # a


# 5.1.3 list comprehension

squares = []
for x in range(10):
    squares.append(x**2)                # regular way to create list

squares = list(map(lambda x: x**2, range(10)))  # list comprehension

squares = [x**2 for x in range(10)]     # list comprehension, equivalent

                                        # creating list based on another list (range(10) here)
                                        # syntax: [expr for 0 or more for or if clauses]

[(x, y) for x in [1,2,3] for in [3,1,4] if x != y]
                                        # [(1,3), (1,4), (2,3), (2,1), (2,4), (3,1), (3,4)]

combos = []
for x in [1,2,3]:                       # equivalent
    for y in [3,1,4]:
        if x != y:
            combos.append((x, y))

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]                      # double
[x for x in vec if x >=0]               # filter
[abs(x) for x in vec]                   # abss

strs = [' asdf ', '    s']
[item.strip() for item in strs]

[(x, x**2) for x in range(6)]           # tuples mast be parenthesized

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]   # flatten the list

from math import pi
[str(round(pi, i)) for i in range(1, 6)] 


# 5.1.4 nested list comprehension

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

[[row[i] for row in matrix] for i in range(4)] # translates rows into columns

transposed = []                         # this is equivalent
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed = []                         # this is also equivalent
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

list(zip(*matrix))                      # there is a built in function zip for that and * also metters
                                        # * unpacks argument lists


# 5.2 del statement

					# used to remove elements from list by their index
a = [-1, 1, 66.24, 333, 333, 1234.5]
del a[0]				# [1, 66.24, 333, 333, 1234.5]
del a[2:4]				# remove slice [1, 66.24, 1234.5]
del a[:]				# remove all

del a					# can also remove entire variable


# 5.3 tuple 
			# lists and strings are sequence data types, tuples are too

t = 1234, 4321, 'hello'			# tuple packing
t[0]					# 1234
t					# (1234, 4321, 'hello')
u = t, (1, 2, 3, 4)			# nested tuples
u					# ((1234, 4321, 'hello'), (1, 2, 3, 4))

			# tuples are immutable
			# but may contain mutable objects

			# access to elements: unpacking (*) or indexing

emptyTuple = ()
singleton = 'single item',		# not comma after single element
len(empty)				# 0
singleton				# ('single item',)

x, y, z = t				# sequence unpacking, item numbers should match
					# multiple assignments is just packing and unpacking


# 5.4 set
			# unordered collection with no duplicates

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)				# {'orange', 'banana', 'pear', 'apple'}
'orange' in basket			# true, fast membership testing
'crabgrass' in basket			# false

# set operations
a = set('abracadabra')
b = set('alacazam')
a					# {'a', 'r', 'b', 'c', 'd'}
a - b					# {'r', 'b', 'd'}
a | b					# {'a', 'c', 'r', 'b', 'c', 'd', 'm', 'z', 'l'}
a & b					# {'a', 'c'}
a ^ b					# {'r', 'b', 'd', 'm', 'z', 'l'}

# set comprehensions similar to list comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
a					# {'r', 'd'}


# 5.5 dictionary
			# kyes should be immutable: string, number, 
			# 	tuple with strings, numbers and valid tuples

dict = {}				# empty dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel					# {'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack']				# 4098
del tel['sape']
list(tel.keys())			# ['jack', 'guido']
sorted(tel.keys())			# ['guido', 'jack']
'guido' in tel				# True
'jack' not in tel 			# False

# constructor
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # {'sape': 4139, 'jack': 4098, 'guido': 4127}
dict(sape=4139, guido=4127, jack=4098)	# {'sape': 4139, 'jack': 4098, 'guido': 4127} - string keys

# dict comprehension
{x: x**2 for x in (2, 4, 6)}		# {2: 4, 4: 16, 6: 36}


# 5.6 looping

# dictionary looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)			# gallahad the pure
					# robin the brave

# sequence index/value looping with enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)			# 0 tic 	1 tac 		2 toe

# looping through 2+ sequences at the same time with zip
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for l, n in zip(questions, answers):
	print('{0} {1}'.format(l, n), end=', ')	# a 1    b 2    c 3

# reverse looping
for i in reversed(range(1, 10, 2)):
	pring(i)			# 9 7 5 3 1

for i in sorted(set([3, 4, 1, 6, 2, 1])):
	print(i)			# 1  2  3  4  6

# it is often simpler to create new list instead of modifing looped one
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, float('NaN')]
filtered_data = []
for v in raw_data:
	if not math.isnan(v):
		filtered_data.append(v)
filtered_data				# [56.2, 51.7, 55.3]

# 5.7 conditions
			# condition can contain any operators

in, not in		# check if value occur in sequence
is, is not		# compare if 2 obj are really the same obj, matters for mutable

			# comparisons have lower priority than numerical operators

			# comparisons can be chained
a < b == c		# tests if a is less than b and b equals c

and, or, not		# lower priority than comparison, betwen them or < and < not
			# and, or are short cirquit operators: 
			# evaluation stops as the outcome is defined

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null		                # 'Trondheim'

			# assignment can not occur inside expressions

# 5.8 comparing sequences and other types

			# sequence objects of the same type can be compared
			# lexicographical ordering
			# strings comparison uses Unicode code point number

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

'----------------------------------------------------------------------------------------------------'


####    6   modules

'----------------------------------------------------------------------------------------------------'

                        # module is a file with python definitions and statements
                        # has name ending with .py
                        # it's name is accessible inside with a global variable __name__

                        # create file test.py with
def a():
    print('a')

def b():
    return 'b'

def p(str):
    print(str)
                        # now in the interpreter or other script/module you can add import it
import test

test.a()                                # a
test.b()                                # 'b'

test.__name__                           # test

a = test.a                              # assigning local name to imported function
a()                                     # a


#   6.1     more on modules

                        # module may contain executable statements inteded to initialize it
                        # they are executed only when module name is encountered first time in import
                        
from test import a, b                   # will import a and b directly, test is not defined/imported
a()                                     # a

from test import *                      # import all names except starting with _
                                        # usually not used as it may hide already defined names

import importlib
importlib.reload(modulename)            # to reload module that was updated during interpreter session


#   6.1.1 executing modules as scripts

python test.py <arguments>              # module is executed, __name__ is test to __main__

                        # add this to the end

if __name__ == "__main__":              # if module is executed, calls p() with first argument
    import sys
    p(sys.argv[1]))
                        # now this module may be both imported or executed by itself
python test.py hello
                        # if this module is imported this code will not run

                        # this is often used for user interfase or testing (executing runs tests)


#   6.1.2   module search path

import test
                        # interpreter first searches built in modules
                        # if not found it searches in derectories listed in sys.path
                        # : directory containing script or current directory if file is not specified
                        # : PYTHONPATH
                        # : installation-dependent default

                        # program may modifi sys.path after initialization
                        # current directory is placed in front of search path


#   6.1.3   compiled python files

                        # Python caches compiled version of each module in the __pycache__ directory
                        # under name module.version.pyc, version is usually a python version
                        # in CPython release 3.3 compiled version of test.py will be
                        # __pycache__/test.cpython-3.3.pyc

                        # python checks date of the module against .pyc file and recompiles if needed
                        # compiled modules are platform independent

                        # compiled and optimized -O, -OO scripts doesn't run fuster, only load faster

                        # module compileall can compile all modules in the directory


#   6.2     standard modules

			# some standard modules are built into interpreter
			# this set it configurable and depends on the platform

import sys				# sys is built 

sys.ps1					# '>>> ' defines primary prompt, can be changed
sys.ps2					# '... ' defines secondary prompt, can be changed
					
sys.path.append('/ufs/guido/lib/python') # way to change path in 


# 6.3 	dir()

			# lists variables, modules, functions, etc.
import test, sys
dir(test)				# ['__name__', 'a', 'b', 'p']
dir(sys)				# all the sys definitions

dir()					# lists all currently defined names

import builtins
dir(builtins)


# 6.4	packages

			# package is a collection of modules
			# way of structuring module namespace by using dotted names

A.B					# designates submodule B in package A

# example of audio files processing package

sound/                          	# Top-level package
      __init__.py               	# Initialize the sound package
      formats/                  	# Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  	# Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  	# Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

			# __init__.py is used to make Python treat directories as containing packages
			# it may be empty file or it may run some initialization code
			
import sound.effects.echo		# imports individual submodule from package
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
					# running function from this package

from sound.effects import echo		# another way to import submodule
echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects.echo import echofilter # importing only one function from submodule
echofilter(input, output, delay=0.7, atten=4)

from package import item		# item may be a submodule(subpackage) of package
					# or it may be a name defined in the package (class, function)
					# import first tests if it's defined in the package
					# next it tries to load it as a module
					# ImportError exception is raized if it failed

import item.subitem.subsubitem		# in this case item and subitem must be packages
					# subsubitem may be a module or package, but not class or var

# 6.4.1	importing * from a package

__all__ = ["echo", "surround", "reverse"] # if __init__.py defines list named __all__
from package import *			# will import 3 named submodules of sound package

			# if __all__ is not defined from import will ensure that package is imported
			# funning __init__.py and then import all names defined in package:
			# names defined by __init__.py

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

from package import submodule		# is recomended way to import unless
					# importing module needs to use submodule with same name
					# from different package


# 6.4.2 intra-package references
			# it's possible to use absolute import paths withing one package for siblings

from sound.effects import echo		# absolute path: can be used in sound.filters.vocoder

from . import echo			# relative path: from surround module
from .. import formats
from ..filters import equalizer

			# relative imports are based on the name of the current module
			# modules used in main module should be imported using absolute path

# 6.4.3 packages in multiple directories

			# special variable __path__ may hold the directory path holding
			# package's __init__.py before code in that file is executed
			# modification of this variable will affect future searches for modules

'----------------------------------------------------------------------------------------------------'


### 	7 input/output

'----------------------------------------------------------------------------------------------------'







'----------------------------------------------------------------------------------------------------'
'----------------------------------------------------------------------------------------------------'



#### other useful things

import random
random.random()     # gives random value from [0, 1)


# filesystem interaction

import os
os.getcwd()		# get current directory path

os.chdir('path')	# chenge current directory

import glob
glob.glob('*.cpp')	# get list of all files in current directory conforming to *.cpp pattern



