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