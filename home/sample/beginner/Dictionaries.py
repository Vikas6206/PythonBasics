# Used to store values in kety value pair kind of like map in Java

# Each key has to be uniques just like the dictionary in real world

customer = {
    "name": "Vikas Kumar",
    "age": 29,
    "is_verified": True
}

# Access each item via [] bracket

print(customer["age"])
# Note the birthday key is not there in the dicctionary and hence sinec we are trying to access it we are getting None instead of error
print(customer.get("birthDay"))

# If we want to assign some default value to the key which doesn't
# exist in Tuple we can do that

print(customer.get("birthDay", "jan 1 1990"))

# We can update the existing dictionary

customer["name"] = "VKK"
print(customer["name"])

# We can add value to the existing dixtionary

customer["sex"] = "Male"
print(customer["sex"])
print(customer)

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

################# Enoji translator ####################
message = input(">")
words = message.split(' ')
emojis = {
    ":)": ":::):::",
    ":(": "::::(:::::"
}
output = ""
for word in words:
    output += emojis.get(word, words) + " "
print(output)
