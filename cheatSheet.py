
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


# 4 Control flow

'----------------------------------------------------------------------------------------------------'

x = int(input("Please enter number: "))	#	- invite to enter integer

'----------------------------------------------------------------------------------------------------'

if 0==0:
	smth
elif 1==1:
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

for w in words:
	print(w, len(w))

for i in range(len(squares))
	print(i, squares[i])

'----------------------------------------------------------------------------------------------------'

for …:
else:

'----------------------------------------------------------------------------------------------------'

