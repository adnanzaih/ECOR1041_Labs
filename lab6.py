#Lab 6
#Student: Adnan Hafeez 101210710

"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Adnan Hafeez 101210710

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?
Yes it does matter. But both are equally valid in creating strings.

Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Hello')
# Type what you see: <class 'str'>

>>> type("goodbye")
# Type what you see: <class 'str'>

>>> 'Hello'
# Type what you see: 'Hello'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# Result/Output: ''

>>> '"Spam, spam, spam," he said.'
# Type what you see: (Nested quotations)
'"spam, spam, spam," he said.'

>>> "I haven't a clue"
# Type what you see: (Nested apostrophe)
"I haven't a clue"

>>> 'I haven't a clue'
# Type what you see: (Nested apostrophe)
'I haven't a clue'
  File "<stdin>", line 1
    'I haven't a clue'
             ^
SyntaxError: invalid syntax

Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?

It depends on what you are writing. If you're righting a word that needs a single quote, it is best to encapsulate the string in double quotes, as to distinguish between the quote types and avoid syntax errors. If you're writing something that requires the reader to read a double quote, it is best to encapsulate the string in a single quote. For example, "you're", or 'Are you "here" yet?'.

==================

Exercise 2: What operations are permitted with values of type str?
Addition (concatenation) and multiplication are permitted.

When used with strings, + is the concatenation operator.

>>> 'Hello, ' + 'world!'
# Type what you see: 'Hello, world!'

When used with strings, * is the replication operator.

>>> "Spam" * 3
# Type what you see:
'SpamSpamSpam'

>>> 3 * "Spam"
# Type what you see: (Reflect: What does this say about order of operators?)
'SpamSpamSpam'

>>> "Spam" * 0
# Type what you see:
''

>>> "Spam" * -3
# Type what you see:
''

There are other operators to try now: - and /

>>> "Hello" - "He"
# Type what you see:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'


>>> 'Spam' / 3
# Type what you see:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'



Concluding Questions: What operators work with strings?  Does the order of operands matter?
Addition (concatenation), and multiplication operators work with strings. The order of the operand's does not matter for multiplication. However it matters for concatenation, for example "Hello" + "World" will print HelloWorld, but "World" + "Hello" will print "WorldHello".

=======================

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123?

>>> '123' + 456
# Type what you see:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str


>>> '123' + '456'
# Type what you see:
'123456'


Concluding Question: When a string looks like a number, is it a number or a string?
When a string looks like a number, it is still a string.
=========
Last edited: October 27, 2020
"""

def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
    return s*n

def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.
    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    """
    return len(s1+s2)


def replicate(string: str) -> str:
    """
    Returns a new string of the input string that is replicated by the number of characters of the input string.

    >>> replicate('a')
    'a'
    >>> replicate('abc')
    'abcabcabc'
    >>> replicate('123')
    '123123123'
    """
    return string*len(string)


# Main Script

#Exercise 4
test1 = repeat('yes',4) # yesyesyesyes
test2 = repeat('no',0) # ''
test3 = repeat('no',-2) # ''
test4 = repeat('yesnomaybe',3) # yesnomaybeyesnomaybeyesnomaybe

print('test1 result = ', test1)
print('test2 result = ', test2)
print('test3 result = ', test3)
print('test4 result = ', test4)

#Exercise 5
test1 = total_length('yes','no') # 5
test2 = total_length('yes','') # 3
test3 = total_length('YES!!!!', 'Noooooo') # 14

print('test1 result = ', test1)
print('test2 result = ', test2)
print('test3 result = ', test3)

#Exercise 6
test1 = replicate('a') # a
test2 = replicate('abc') # abcabcabc
test3 = replicate('123') # 123123123
test4 = replicate('Carleton Engineering') #Carleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton EngineeringCarleton Engineering


print('test1 result = ', test1)
print('test2 result = ', test2)
print('test3 result = ', test3)
print('test4 result = ', test4)


# Do not put any code below this line
print("End of file reached successfully.")
# Note that if this message isn not printed when you run your script, there is an error in your script.