'''
-------------Type Conversions-------------
# Converting one data type into another data type.

String-->List
String-->Float

#Explicit Type Conversion --> Manually changing the datatype

'''
#int()
a="100" # It is in string data type.
print(int(a))

#float()

b="578"
print(float(b))

#string

c=45
print(c)   #integer
print(str(c))  # string

#boolean

print(bool(1)) #true
print(bool(0)) #false
print(bool("")) #fals if no message inside the double quotes
print(bool("python")) #true if message is passed inside the double quotes

#List

text="python"
print(list(text))

# Implicit Type Conversion
# Python compiler autmatically converts one data type to other

x=10 #integer type
y=10.5 #float data type
print(x+y)

'''
x=10
y=14.5

10.0
10.5

'''