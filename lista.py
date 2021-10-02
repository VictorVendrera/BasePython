
#################################1#######################
zoo_animals = ["pangolin", "cassowary", "sloth", "lion"];
# One animal is missing!

if len(zoo_animals) > 3:
  print( "The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])

#########################################2#############################
#exemplos
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print (animals) # Observe what prints after the insert operation

#################################3###################

my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    print(2 * number)


#######################################4############################
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print( square_list)

######################################5##############################
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print (residents['Sloth'])
print (residents['Burmese Python'])

#############################################6###########################
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print( menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)