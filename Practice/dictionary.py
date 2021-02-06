new_dict = {
    "brand": "Honda",
    "model": "Civic",
    "year": 1995
}
print(new_dict)
x = new_dict["brand"]
print(x)
new_dict["year"] = 2020
print(new_dict)
# print all key names in the dictionary
for x in new_dict:
    print(x)
print("*****")
# print all values in the dictionary
for x in new_dict:
    print(new_dict[x])
# loop through both keys and values
for x, y in new_dict.items():
    print(x, y)
