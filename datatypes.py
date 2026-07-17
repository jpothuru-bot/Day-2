'''
-------------- Data types -----------------

--> A data type tells python what kind of value a variable


'''
#string  can be define in single/double/triple quotes.

a="apple"
b=20
c=34.4
is_cricketer=True #boolean two values True/False.
d=4+6j #complex data type --> combination of i+j

print(type(a))
print(type(b))
print(type(c))
print(type(is_cricketer))
print(type(d))

'''
1. Integer(int)
'''
b=20
print(type(b))

'''
2.Float
'''
c=34.84
print(type(c))

'''
List
# A list is an ordered,mutable(changeable)collection of elements.
# It can store different types of data types such as integers,strings,and floats.
Lists are created using square brackets[].

x=[10,20,30,40]
y=["apple","mango","banana"]
z=[10,20,56,"apple",true]

Tuple
# A tuple is an ordered,immutable(unchangeable)collection of elements.
# It can store different types of data and is created using parantheses()

x=(10,20,30,40)
y=("apple","mango","banana")

Dictionary
# A Dictionary is a mutable(changeable)unordered collection of key value pairs.
# It is created using curly braces {},where each key is unique and maps to a value.

d={
# key:value pair
'''
d={
    "name":"jayanth",
    "age":20,
    "course":"python"
}
print(d)

'''
Set
# A set is an unordred,mutable collection of unique elements.
# It is created using curly braces {} or the set().
# A set does not allow duplicat values.

'''
s={10,20,30,40,}
print(s)