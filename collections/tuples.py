# import namedtuple from the collections module
from collections import namedtuple

# create tuple of our ages
our_ages = (40, 37)

# create named tuple defining attribute names
Ages = namedtuple('Ages', ['Rob', 'John'])
# assign values to the names of the named tuple
our_ages_named = Ages(40, 37)

# print ages from tuple
print("our ages are:", our_ages)

#printing ages from tuple with iterator
print("printing our ages using an iterator")
for i in our_ages:
    print(i)

#print ages with keys(?) from named tuple 
print("our ages named are:", our_ages_named)

# printing the named tuple using an iterator
print("printing the named ages using an iterator:")
for name in our_ages_named._fields:
    print(name, "=>",  getattr(our_ages_named, name))

