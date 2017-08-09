list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

product = ['pizza','chocklate','pencil','rubber']
price = [49,45,10,5]

# first way 
dict1 = {}
dict1 =  dict(zip(list1, list2))
print dict1

# second way creating dictionary
dict2 = {}
for key in product:
	for value in price:
		dict2.update({key:value})
print dict2

# third way of creating dict
dict3 = {}
for key in product:
	for value in price:
		dict3[key] = value
print dict3

# update dictionary
dict2.update({'duster':30})
print dict2


# check whether key is present or not
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print(x,'Key is present in the dictionary')
  else:
      print(x,'Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# add values to dictionary
product_dict = {'rubber': 5, 'pencil': 5, 'chocklate': 5, 'duster': 30, 'pizza': 5}
def add_key_value(key,value):
	if key not in product_dict:
		product_dict.update({key:value})
		print "key added to dictionary"
		print product_dict
add_key_value('rubber',10)
add_key_value('chalk',40)

# delete key from dictionary
def del_key(key):
	if key in product_dict:
		del product_dict[key]
		print "key is deleted from dictionary"
		print product_dict
del_key('rubber')

# update value in dictionary 
def update_value(key,value):
	if key in product_dict:
		product_dict[key] = value
		print "value is updated related to key in dictionary"
		print product_dict
update_value('pencil',30)

# first method to iterate over dictionaries
print "iterate dictionary ===="
for k,v in product_dict.items():
	print k,v

# second method to iterate over dictionaries
for k,v in product_dict.iteritems():
	print k,v

