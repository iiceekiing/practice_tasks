#A list is an ordered, mutable (changeable) collection of elements in Python.

fruits = ['apple', 'banana', 'cherry']



"""
✅ Features:
Ordered (keeps insertion order)

Allows duplicates

Mutable (can change values)

Can store any data type (mixing allowed)

"""


#🔧 Common Operations

#1. Accessing Elements (Indexing)

print(fruits[0])      # 'apple'
print(fruits[-1])     # 'cherry'


#2. Slicing

print(fruits[0:2])    # ['apple', 'banana']
print(fruits[::2])    # ['apple', 'cherry']


#3. Modifying Lists

fruits[1] = 'mango'
print(fruits)
fruits.append('orange')
print(fruits)
fruits.insert(1, 'kiwi')
print(fruits)
fruits.pop() # Removes last item
print(fruits)
fruits.remove('kiwi') # Removes by value
print(fruits)

#4. Length and Existence

print(len(fruits))
print('kiwi' in fruits)



#5. Loops

for item in fruits:
    print(item)

