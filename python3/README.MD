# 1. PYTHON CRASH COURSE, 3RD EDITION
[Link](/python/python-crash-course-3rd/)


## Data Types and Var

### Variables

- Naming and Using Variables

  -	 Variable names can contain only letters, numbers, and underscores and only start with a letter or an underscore.

  -	 Avoid using Python keywords and function names as variable names.

  -	 Be careful when using the lowercase letter l and the uppercase
  letter O because they could be confused with the numbers 1 and 0.

### Strings

- `'This is a string in python'`

- `"This is another string in python"`

### Numbers

- `Integer` and `Float`

#### Abs Function

- This function is used to return the absolute value of a number.

```
a = -1.23
print(abs(a))

# This program’s output will be as follows:
1.23
```

#### Ceil Function

- This function is used to return the ceiling value of a number.

```
import math


a = 1.23
print(math.ceil(a))

# This program’s output will be as follows:
2
```

#### Max Function

- This function is used to return the largest value in a set of numbers.

```
print(max(3,4,5))

# This program’s output will be as follows:
5
```

#### Min Function

- This function is used to return the smallest value in a set of numbers.

```
print(min(3,4,5))

# This program’s output will be as follows:
3
```

#### Pow Function

- This function is used to return the value of x to the power of y, where the syntax is ‘pow(x,y)’.

```
print(pow(2,3))

# This program’s output will be as follows:
8
```

#### Sqrt Function

- This function is used to return the square root of a number

```
import math


print(math.sqrt(9))

# This program’s output will be as follows:
3.0
```

#### Random Function

- This function is used to simply return a random value.

```
import random


print(random.random())

# This program’s output will be as follows:
0.0054600853568235691
```

#### Randrange Function

- This function is used to return a random value from a particular range.

```
import random


print(random.randrange(1,10,2))

# This program’s output will be as follows:
5
```

#### Sin Function

- This function is used to return the sine value of a number. 

```
import math


print(math.sin(45))

# This program’s output will be as follows:
0.8509035245341184
```

#### Cos Function

- This function is used to return the cosine value of a number. 

```
import math


print(math.cos(45))

# This program’s output will be as follows:
0.5253219888177297
```

#### Tan Function

- This function is used to return the tangent value of a number.

```
import math


print(math.tan(45))

# This program’s output will be as follows:
1.6197751905438615
```

### Boolean

- `True` and `False`

### List 

- `month = ['Jan', 'Feb', 'March', 'And so on!']`

### Tuples

- `numbers = (19, 21, 28, 10, 11)`

### Sets

### Unpacking

```
ages = (25, 30, 35, 40)
Drake, Emma, Sully, Sam = ages
```

### Python Dictionaries

- `AlumniAge = {'Andrea': 23, 'John': 28}`

```
clear(): Remove all items from the dictionary.
copy(): Return a shallow copy of the dictionary.
fromkeys(seq[, v]): Return a new dictionary with keys from seq
and value equal to v (defaults to None).
get(key[,d]): Return the value of key. If the key does not exist,
return d (defaults to None).
items(): Return a new view of the dictionary’s items (key, value).
keys(): Return a new view of the dictionary’s keys.
pop(key[,d]): Remove the item with a key and return its value or
return ‘d’ if the key is not found. If d is not provided and the key is
not found, raises KeyError.
popitem(): Remove and return an arbitrary item (key, value).
Raises KeyError if the dictionary is empty.
setdefault(key[,d]): If the key is in the dictionary, return its value.
If not, insert key with a value of d and return d (defaults to None).
update([other]): Update the dictionary with the key/value pairs
from other, overwriting existing keys.
values(): Return a new view of the dictionary’s value

There are also some embedded functions that can be used with a dictionary.
all(): Return True if all keys of the dictionary are true (or if the
dictionary is empty).
any(): Return True if any key of the dictionary is true. If the
dictionary is empty, return False.
len(): Return the length (the number of items) in the dictionary.
cmp(): Compares items of two dictionaries.
sorted(): Return a new sorted list of keys in the dictionary
```

### Operators in Python

#### Arithmetic Operators

##### Sum Operator `(+)`:  `6 + 4` = `10`

##### Subtract Operator `(-)`:  `4 – 3` = `1`

##### Multiplication Operator `(*)`:  `3 * 2` = `6`

##### Division Operator `(/)`:  `3.5 / 2` = `1.75`

##### Module Operator `(%)`:  `8 % 5` = `3`

##### Exponent Operator `(**)`:  `3 ** 2` = `9`

##### Whole Division Operator `(//)`:  `3,5 // 2` = `1.0`

#### Comparison Operators
- The comparison operators are those that will be used to compare values and return; as a result, the True or False response as the case may be, as a result of the condition applied.

##### Operator Equal to: `( == )`:  `3 == 3` >>> `True`,  `5 == 1` >>> `False`

##### Operator Different than `( != )`:  `3 != 4` >>> `True`,  `3 != 3` >>> `False`

##### Operator Greater than `( > )`:  `5 > 3` >>> `True`,  `3 > 8` >>> `False`

##### Operator Less than `( < )`:  `3 < 5` >>> `True`,  `8 < 3` >>> `False`

##### Operator `( >= )`:  `8 >= 8` >>> `True`,  `3 >= 8` >>> `False`

##### Operator `( <= )`:  `8 <= 8` >>> `True`,  `10 <= 8` >>> `False`

#### Logical Operators

- Logical operators are the `and`, `or`, `not`. Their main function is to check if two or more operators are true or false, and as a result, returns a True or False. `12 % 6 == 0 or 12 % 8 == 0` >>> `True`



