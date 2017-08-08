# Accessing Values in Dictionary:

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# Updating Dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

# Delete Dictionary Elements
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']; # remove entry with key 'Name'
print dict
dict.clear();     # remove all entries in dict
print dict
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict
del dict       # delete entire dictionary
print dict

# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']

# Check whether key is present or not
dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.has_key('Age')
print "Value : %s" %  dict.has_key('Sex')

