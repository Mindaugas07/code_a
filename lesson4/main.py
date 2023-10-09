# print("something")

# weight_lower_limit: float = 80.0
# weight_higher_limit: float = 100.0

# user_weight = float(input("Enter your weight: "))

# if user_weight > weight_higher_limit:
#     if user_weight > 125.5:
#         print("King Kong")
#     print("Kebab")
# elif user_weight < weight_lower_limit:
#     print("Not kebab")
# else:
#     print("All good")




# list_empty = []
# tuple_empty = ()
# number = float(input("Enter a number: "))
# list_empty.append(number)
# tuple_empty += (number, )
# number_two = float(input("Enter a number: "))
# tuple_empty += (number_two, )
# list_empty.append(number_two)
# number_three = float(input("Enter a number: "))
# tuple_empty += (number_three, )
# list_empty.append(number_three)

# print(list_empty, tuple_empty)

# Create a program, which takes 10 random numbers. The program should producea list of non primary and tuple of primary numbers.
# After input is done, program should return the the mathematical differnce between the highest and lowest 
# # number from non primary numbers, and sum of primary numbers from tuple.
# numbers_list = []
# number = float(input("Enter a number: "))

# for number in 10:
#     print("122")
# ten_random_numbers = float(input("Enter ten random numbers: "))

# Create a program, which takes 10 random numbers as user inputs.The program should produce
# list of input values what are less than 50 and tuple of all other values.After input is done,
# program should return the the mathematicaldiffernce between the highest and lowest number from
# non primary numbers, and sum of primary numbers from tuple.

# number_list = []
# number_tuple = ()
# number_one = float(input("Enter a number: "))
# if number_one < 50:
#     number_list.append(number_one)
# else:
#     number_tuple += (number_one, )

# number_two = float(input("Enter a number: "))
# if number_two < 50:
#     number_list.append(number_two)
# else:
#     number_tuple += (number_two, )

# number_three = float(input("Enter a number: "))

# if number_three < 50:
#     number_list.append(number_three)
# else:
#     number_tuple += (number_three, )

# number_four = float(input("Enter a number: "))

# if number_four < 50:
#     number_list.append(number_four)
# else:
#     number_tuple += (number_four, )

# number_five = float(input("Enter a number: "))

# if number_five < 50:
#     number_list.append(number_five)
# else:
#     number_tuple += (number_five, )

# number_six = float(input("Enter a number: "))

# if number_six < 50:
#     number_list.append(number_six)
# else:
#     number_tuple += (number_six, )

# number_seven = float(input("Enter a number: "))

# if number_seven < 50:
#     number_list.append(number_seven)
# else:
#     number_tuple += (number_seven, )
# number_eight = float(input("Enter a number: "))

# if number_eight < 50:
#     number_list.append(number_eight)
# else:
#     number_tuple += (number_eight, )

# number_nine = float(input("Enter a number: "))

# if number_nine < 50:
#     number_list.append(number_nine)
# else:
#     number_tuple += (number_nine, )
# number_ten = float(input("Enter a number: "))
# if number_ten < 50:
#     number_list.append(number_ten)
# else:
#     number_tuple += (number_ten, )

# print(number_list, number_tuple)

# print("Diference between the highest and lowest numbers in list: ", max(number_list) - (min(number_list)))

# sum = 0

# for number in number_tuple: sum += number

# print("The sum of tuple numbers: ", sum)


# empty_list = []
# number_tuple = ()
# for number in range(10):
#     number_new = float(input("Enter a number: "))
#     if number_new < 50:
#         empty_list.append(number_new)
#     else:
#         number_tuple += (number_new, )


# print(empty_list, number_tuple)

# print("Diference between the highest and lowest numbers in list: ", max(empty_list) - (min(empty_list)))

# sum = 0

# for number in number_tuple: sum += number

# print("The sum of tuple numbers: ", sum)

# user_information = {"name": None, "surname": None, "age": None}
# name_entered = input("Please enter your name: ")
# surname_entered = input("Please enter your surname: ")
# age_entered = input("Please enter your age: ")
# user_information["name"] = name_entered
# user_information["surname"] = surname_entered
# user_information["age"] = int(age_entered)
# print(user_information)

# if user_information["age"] >= 21:
#     print("You can enter an online casino.")
# else:
#     print("You are too young to enter an online casino.")

# list_priveleged_users = ["Jonas", "Tomas"]
# user_name = input("Enter your name: ")
# if user_name in list_priveleged_users:
#     print(f"Welcome {user_name}")
# else:
#     print("Welcome ")

# first_number = input("Please enter first number: ")
# second_number = input("Please enter second number: ")
# if first_number > second_number:
#     print("First number is higher ")
# elif first_number == second_number:
#     print("Numbers are equal ")
# else:
    # print("Second number is higher ")


# import operator

# ops = {
#     '+' : operator.add,
#     '-' : operator.sub,
#     '*' : operator.mul,
#     '/' : operator.truediv, 
#     '%' : operator.mod,
#     '^' : operator.xor,
# }

# first_number = int(input("This is a small callculator for doing simple operations. Please enter first number: "))
# second_number = int(input("Please enter second number: "))
# operation = input("Please enter operation sign: ")

# if operation == "+":
#     outcome = int(first_number) + int(second_number)
#     print(outcome)
# elif operation == "-":
#     outcome = int(first_number) - int(second_number)
#     print(outcome)
# elif operation == "*":
#     outcome = int(first_number) * int(second_number)
#     print(outcome)
# elif operation == "/":
#     outcome = int(first_number) / int(second_number)
#     print(outcome)
# else:
#     print("You have entered a bad operation sign: ")
# outcome = ops[operation](int(first_number), int(second_number))

# print(outcome)

# import random

# number_guess = input("Guess a number from 1 to 10: ")
# random_number = random.randint(1, 10)

# if number_guess == random_number:
#     print("You guessed it! Bravo!")
# else:
#     print(f"Not this number. Correct number was {random_number}")