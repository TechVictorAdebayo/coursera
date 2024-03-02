
# creating a tuple of my favourite book
book = ("Lord of the rings","Purple Hibiscuss", "A woman in Her Prime", "You've already got it", "Faith for Healing" )

for fav in book:
    print(fav)

#Creatinga dictionary that takes imput from the user

person_info = {}

#Ask the user for info and stor in a dictionary
person_info["name"] = input('Enter your name: ')
person_info["age"] = int(input("Enter your age: "))
person_info["favourite_color"] = input ("Enter your favourite color: ")
person_info["height"] = float (input ("Enter your height: "))
person_info["gender"] = input ("Whats your  gender? ")

#Print the info
print("Information about the person: ")



word_list = ["apple", "banana", "orange", "kiwi", "pineapple", "grape"]

#Using list comprehension
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

#Print
print("Original list of words: ", word_list)
print("List of words with odd number of characters: ", odd_length_words)
