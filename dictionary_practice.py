dictionary = {
    'player name': 'star_destroyer',
    'ranking': [1287],
    'positive_kd': False
}

print(dictionary['player name']) # will print star_destroyer


# for the key values in dictionary, you can use strings, boolean, and numbers
# key needs to be immutable, so it cant change, thats why we cant use lists for key value

# dictionary methods - a good way to access a key to see if it exists is to use .get
# ex
print(dictionary.get('power')) # this will return None
# you can also do print(dictionary.get('power', 100)) - by adding the 100, your adding a default value
# ex- if power level is not found, it will make 100 the power level by default, but if power is assigned already, it will use og

# another way of creating a dictionary ----

players = dict(name='young_vader25')
print(players)

# we can use 'in' with dictionary to view if certain things can be found in them
#ex

print('power' in dictionary.keys()) # will check if power is one of the keys in the dict
print('power' in dictionary.values()) # same thing but for values

# other dict methods

# print(dictionary.clear()) this will empty the dictionary - same thing for doing:
# dictionary.clear()
# print(dictionary) 
# dictionary will be empty

#copy
players_nextgen = players.copy()
print(players_nextgen) # will copy a dictionary

# pop will remove key and value from dictionary
# ex print(user.pop('name of key you want elimanted'))

# popitem - pops up last key and value

# update will update a key value
# ex
print(dictionary.update({'positive_kd':True}))
print(dictionary)