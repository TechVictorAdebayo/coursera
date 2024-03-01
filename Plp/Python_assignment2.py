# creating an empty list
my_list = []

#appending into my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert the value 15 at the second position in the list
my_list[1] = 15

#Extend my list  with another list [50, 60, 70]
my_list.extend ([50, 60, 70])

#Remove the last element from my_list

my_list = my_list[:-1]

#sort my_list in ascending order 

my_list.sort()

#Find and print the index of the value of 30 in my_list

index = my_list.index(30)
print("Index of 30 in my_list:", index)
print(my_list)
