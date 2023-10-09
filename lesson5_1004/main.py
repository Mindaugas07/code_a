# print("weeeee")


# my_dictionary = {"name": "Mindaugas", "surname": "Vytautas"}
# print(my_dictionary["name"])
# del my_dictionary["surname"]
# print(my_dictionary)

# print(my_dictionary.keys())

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 200, 'd': 400}
# d1.update(d2)
# print(d1)

# d = {'a': 10, 'b': 20, 'c': 30}
# for key, value in d.items():
#     print(key, value)

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)

# empty_somethin = {}
# print(type(empty_somethin))

# new_dictionary = {}
# new_dictionary["name"] = input("Please enter your name: ")
# new_dictionary["surnamename"] = input("Please enter your surnamename: ")
# new_dictionary["age"] = input("Please enter your age: ")
# print(new_dictionary)

# world = {
#     "Continents": {
#         "Africa" : "Morocco",
#         "Europe" : "Lithuania",
#         "Asia" : "Japan",
#         "N. America" : "USA",
#         "S. America" : "Brazil",
#         "Antartica" : None
#         },
#     "Oceans": ["Arctic", "Atlantic", "Indian", "Pacific"]
# }

# world["Continents"]["Atlantida"] = None
# world["Lakes"] = ["Baikal", "Victoria"] 
# oceans = world["Oceans"]
# oceans.append("Deep Waters")
# world["Oceans"] = oceans

# print(world)

# for continent, country in world["Continents"].items():
#     print(country)

# for ocean in world["Oceans"]:
#     print(ocean)

# def cigar_party(cigars, is_weekend):
#   if 39 < cigars < 61 and not is_weekend:
#     return True
#   elif 39 < cigars and is_weekend:
#     return True
#   else:
#     return False
# cigar_party(38, True)
