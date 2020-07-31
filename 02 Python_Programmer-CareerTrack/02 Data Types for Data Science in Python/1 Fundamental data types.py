#Manipulating lists for fun and profit

# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden','Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names2=['Rowen','Sandeep']
baby_names.extend(baby_names2)

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)


#Looping over lists

# Create the empty list: baby_names
baby_names = []


#records is a list of list and the name of the baby is present at fourth location in list 
# Loop over records 
for items in records:
    # Add the name to the list
    baby_names.append(items[3])
    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)


#Using and unpacking tuples

# Pair up the girl and boy names: pairs
pairs = zip(girl_names,boy_names)

# Iterate over pairs
for idx,pair  in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))


#Making tuples by accident
#Tuples are very powerful and useful, and it's super easy to make one by accident. All you have to do is create a variable and follow the assignment with a comma. This becomes an error when you try to use the variable later expecting it to be a string or a number.

#You can verify the data type of a variable with the type() function. In this exercise, you'll see for yourself how easy it is to make a tuple by accident.

# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))


#Finding all the data and the overlapping data between sets

#One quirk in the baby names dataset is that names in 2011 and 2012 are all in upper case, while names in 2013 and 2014 are in title case (where the first letter of each name is capitalized). Consequently, if you were to compare the 2011 and 2014 data in this form, you would find no overlapping names between the two years! To remedy this, we converted the names in 2011 to title case using Python's .title() method.

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))


#Determining set differences
# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)