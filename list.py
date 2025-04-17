my_list = []

# Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
my_list.extend([50, 60, 70])

my_list.pop()
my_list.sort()

# Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
#printing my list
print("my list is:", *my_list, sep=",")
