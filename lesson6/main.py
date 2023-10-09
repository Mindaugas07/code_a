# print("Weee")

# list_of_various_object_types = ["45", 47, ["weee", "ooo"], (1, 2, 6), {"miestas": "Alytus"}, 45.3, True, {"ok", "no"}, ]

# for objektas in list_of_various_object_types:
#     print(type(objektas))

# print(f"There are {len(list_of_various_object_types)} diferent types objects in the list.")

# print(*list_of_various_object_types, sep="#")

# list_with_floats = [45.254, 65.523, 4.000]
# empty_list_with_floats = []

# for floatas in list_with_floats:
#     empty_list_with_floats.append(round(floatas, 2))

# print(empty_list_with_floats)

# list_with_student_names = ["Vytautas", "Kestutis", "Algirdas", "Jogaila", "Gediminas"]
# print(sorted(list_with_student_names))

# def rounding (float_number, skaicius_po_kableio):
#     new_number = round(float_number, skaicius_po_kableio)
#     print(new_number)
# rounding(4.45, 1)

# print(bin(45456465465465465465465465465465465465465465465465))

# float_string = input("Please give me a float ")

# try: 
#     float(float_string)
#     if float(float_string) % 1 != 0: 
#         print(round(float(float_string), 2))
#     else:
#         print("NOT FLOAT!!")
# except:
#      print("NOT FLOAT!!")

# We've got a very long string, containing a bunch of User IDs.
#  This string is a listing, which seperates each user ID with a comma and a whitespace ("' ").
#  Sometimes there are more than only one whitespace.
#  Keep this in mind! Futhermore, some user Ids are written only in lowercase,
#  others are mixed lowercase and uppercase characters.
#  Each user ID starts with the same 3 letter "uid", e.g. "uid345edj".
#  But that's not all! Some stupid student edited the string and added some hashtags (#).
#  User IDs containing hashtags are invalid, so these hashtags should be removed!

# test.assert_equals(get_users_ids("uid12345"), ["12345"])
# test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
# test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
# test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
# test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

# test.describe("Advanced tests")
# test.assert_equals(get_users_ids("uid##doublehashtag"), ["doublehashtag"])
# test.assert_equals(get_users_ids("  uidin name whitespace"), ["in name whitespace"])
# test.assert_equals(get_users_ids("uidMultipleuid"), ["multipleuid"])
# test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])
# test.assert_equals(get_users_ids(" uidT#e#S#t# "), ["test"])

# Task
# 1 Remove all hashtags
# 2 Remove the leading "uid" from each user ID
# 3 Return an array of strings --> split the string
# 4 Each user ID should be written in only lowercase characters
# 5 Remove leading and trailing whitespaces

# user_ids = "uid345e#j'  uid345EDJuid'    uid345edj'   uid3#edj  "
# user_ids = " uidT#e#S#t# "
# user_ids_list_two = []
# user_ids = user_ids.replace("#", "")
# user_ids = user_ids.lower()
# if user_ids[0] == "u":
#     user_ids = user_ids.replace("uid", "", 1)
# user_ids = user_ids.replace(" uid", " ")

# user_ids_list = user_ids.split(",")
# for narys in user_ids_list:
#     if narys[0] != " ":
#         user_ids_list_two.append(narys)
#     else:
#         user_ids_list_two.append(narys.replace(" ", ""))
# print(user_ids_list_two)

# def get_users_ids(string):
#     return [w.replace("uid", "", 1).strip() for w in string.lower().replace("#", "").split(",")]

# get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs")