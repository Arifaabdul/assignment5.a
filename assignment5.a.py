# Task:

# 1. What is dict in python?
'''A dictionary is a kind of data structure that stores items in key-value pairs. 
A key is a unique identifier for an item, and a value is the data associated with that key. 
Dictionaries often store information such as words and definitions, but they can be used for much more. 
Dictionaries are mutable in Python, which means they can be changed after they are created. 
They are also unordered, indicating the items in a dictionary are not stored in any particular order.'''

# 2. Types of dict in python?
''' defaultdict: as the name says, we can give a default value for the currently nonexisting key.
    OrderedDict: keys ordering are guaranteed (based on insertion order)
    Counter: calculate frequency of items. The item must be able to be a key in a dictionary (hashable).
    ChainMap: a way to group together different dictionaries, order matters
    UserDict: base class to create a custom dictionary'''

# 3. What is slicing in dict in python?
'''Slicing a dictionary means obtaining the subsets of the dictionary using the key-value pairs. 
There are many ways to do that but those techniques are lengthy and confusing, we are going to use a module known as itertools, 
using this module, slicing a dictionary is very easy.'''

# Tasks:

# 3. Create a dict with your family members(at least 10 names)?
# expected output : { "family_members" : your family member details}

fam_mem={"family_members":["Samad", "Aktharunnisa", "Anwar", "Arifa", "Asma", "Sheerin", "Azeem", "Fareed", "Fazeelath"]}
print(fam_mem)


# 4: Create a dict with your family members and relations(at least 10 names and relations)?
# Expected output: { "family_members" : your family member details , "relations": your relation with your family member}
# write a program to print your father name?
# write a program to print your favorite family member name?

fam_mem1={"family_member": ["Samad", "Aktharunnisa", "Anwar", "Asma", "Sheerin", "Azeem", "Fareed", "Fazeelath"], "relations": [
    "Father", "Mother", "Elder Brother", "Sister", "Sister in Law", "Younger Brother", "Brother in Law", "Doughter"]}
print(fam_mem1["family_member"][0])
print(fam_mem1["family_member"][-1])

# 5: Create a your friend names and their quality(at least 10 names)?
# Expected output: {"friend_names" : your friend names, "quality" : your friend quality}
# Example output: {"friend_names": ["ravi","shekar", "abbas","jhonny"], "quality" : ["talk active", "anger", "intelligent", "funny"]}
# write a program to print your intelligent friend name?
# write a program to print your best friend name?

friends={"friend_names":["Lalitha","Mounika","Harsha","SaiLakshami","Supriya","Bindu","Anusha","Supriya","Raji","Kamala"], "quality" :[
     "anger", "intelligent", "funny","active", "anger", "smart", "funny", "anger", "talented", "funny"]}
print(friends["friend_names"][1])
print(friends["friend_names"][3])

# 6: Create a your favorite food names and your rating(at least 10 names)?
# Expected output: {"veg_items" : food names, "rating" : your rating}
# {"nonveg_items" : food names, "rating" : your rating}
# write a program to print your rating 1 food name?
food={"veg_items":["Veg Biryani","Veg Manchurian","Veg FriedRice","Veg Salad", "Palak Paneer", "Mattar Paneer", "Gobi Manchurian", "Dal Makhani",
            "Pav Bhaji", "Paneer Tikka Masala"],"rating":[1,3,4,6,7,9,10,2,5,8]}
print(food["veg_items"][0])

# 7: Create a your favorite destination(cities) names and your rating(at least 10 names)?
# Expected output: {"destination" : cities name, "rating" : your rating}
cities={"destination":["Vijayawada","Hyderabad","Vizag","Banglore","turkey","Sydney","Kerala","Mumbai","Delhi","Chennai"],"rating":[
    1,3,4,6,7,9,10,2,5,8]}

# 8: Create a your favorite destination(cities) names and your rating(at least 10 names)?
# Expected output: {"destination" : cities name, "rating" : your rating}
# write a program to print your rating 3 city name?
destinations={"destination":["Vijayawada","Hyderabad","Vizag","Banglore","turkey","Sydney","Kerala","Mumbai","Delhi","Chennai"],"rating":[
    1,3,4,6,7,9,10,2,5,8]}
print(destinations["destination"][1])
