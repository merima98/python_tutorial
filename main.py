# # 1) Arcade Day Pass Tracker - Challlenge Steps

# #Create variables to store:
# #  - customer name
# #  - number of passes
# #  - tokens per pass
# #  - price per pass
# #  - tokens required per game

# customer_name = "Alice"
# number_of_passes = 3
# tokens_per_pass = 50
# price_per_pass = 12.50
# tokens_per_game = 4



# #Calculate:
# #  - total tokens
# total_tokens = number_of_passes * tokens_per_pass
# #  - total cost
# total_cost = number_of_passes * price_per_pass
# #  - games available (use 'floor division' to get a whole number)
# games_available = total_tokens // tokens_per_game

# # 3) Print a summary with :
# #  - customer name
# #  - passes bought
# #  - total tokens
# #  - total cost
# #  - games available

# print('Customer Name:', customer_name)
# print('Passes Bought:', number_of_passes)
# print('Total Tokens:', total_tokens)
# print(f'Total Cost: {total_cost:.2f}')
# print('Games Available:', games_available)


# # User Input Section
# name=input('What is your name?:')
# age=input('How old are you? ')
# print('Hello, ' + name + '! You are ' + age+ ' years old.')



# #2) Calculator

# num1=input('Enter a digit: ')
# num2 = input('Enter second digit: ')

# answer = float(num1) + float(num2)
# print('The answer is: ' + str(answer))



# # 3)Create a distance converter converting km to miles
# # Take two inputs from user: Their first name and the distance in km
# # Print: Greet user by name and show km, and mile values
# # 1 mile is 1.609 kilometers
# # Hint: user correct types for calculating and print
# #  Did you capitalize the name

# first_name = input('Enter your first name: ')
# distance_km = input('Enter distance in kilometers: ')


# mile_to_km = 1.609
# total_mile = float(distance_km) / mile_to_km

# print('Hello, ' + first_name.capitalize() + '! ' + distance_km + ' kilometers is equal to ' + str(round(total_mile, 2)) + ' miles.')

# # Title will also capitalize the name
# print(f'Hi {first_name.title()}!')


# # 4) 
# print('Basic Arithmetic')

# a = 10
# b = 3

# print('Addition: ', a + b)
# print('Subtraction: ', a - b)
# print('Multiplication: ', a * b)
# print('Division (float): ', a/b)
# print('Division (floor): ', a//b)
# print('Modulus: ', a%b)
# print('Exponent: ', a**b)




# # 5)
# # From the string "Welcome to Python 101: Strings", extract text and create/print a new string that says
# # * "1 Welcome Ring to Tyler"
# # * Every first letter in a word should be capitalized (title format)

# # 2. Print the same string backwards...
# #  Hint: Google is you frined

# original_string = "Welcome to Python 101: Strings"
# new_string =original_string[18] + ' ' +  original_string[:8] + original_string[25:29] +  original_string[7:10] + ' Tyler'
# print('All words are capitalized:', new_string.title())

# # Print the original string backwards
# print('Original string backwards:', original_string[::-1])


# # 6)
# # Strings: Find/replace, string formatting

# msg = 'Welcome to Python 101: Strings'
# print(msg.replace('Python', 'C'))  # Find the position of the word 'Python'

# msg1 = msg.replace('Python', 'C')
# print(('Python' in msg))  # Check if 'Python' is in the original message

# name ='TERRY'
# color = 'RED'

# msg2 = '[' + name.capitalize() + '] loves the color ' + color.lower() + '!'

# print(f'{name.capitalize()} loves the color {color.lower()}!')
# print(msg2)  # Print the formatted message


# # 7)
# # Pit stop timing optimizer

# # 1. Ask the user for the total race time in seconds
# # 2. Ask how many pit stops were made.
# # 3. Ask for the average pit stop duration (in seconds).

# # Then:
# # - Calculate the total pit stop time.
# # - Calculate the percentage of the race spent in the pits.


# # Finally, print all of the following:
# # - Total pit stop time in seconds
# # - Percentage of race time spent in pits
# # - A final message if pit time > 5 seconds of the race: "You need a new out crew!"


# total_race_time_in_seconds = float(input('Enter the total race time in seconds: '))
# number_of_pit_stops = int(input('Enter the number of pit stops made: '))
# pit_stop_duration_in_seconds = float(input('Enter the average pit stop duration in seconds:'))


# total_pit_stop_time = number_of_pit_stops * pit_stop_duration_in_seconds

# percentage_of_race_in_pits = (total_pit_stop_time / total_race_time_in_seconds) * 100
# percentage_of_race_in_pits = round(percentage_of_race_in_pits, 2)

# print(f'Total pit stop time in seconds {total_pit_stop_time:.2f}')
# print(f'Percentage of race time spent in pits: {percentage_of_race_in_pits}%')

# if percentage_of_race_in_pits > 5:
#     print('You need a new pit crew!')


# # 8) Lists
# friends = ['Alice', 'Bob', 'Charlie', 'David']

# print('List: ', friends)

# # List - Exercise:

# #  - You sell lemonade over two weeks, the lists show number of lemonades sold per week
# #  - Profit for each lemonade sold is 1.5$

# #  - Add another day to week 2 list by capturing a number as input
# #  - Combine two lists into the list called 'sales'
# #  - Calculate/print how much you have earned on:
# #  - Best day
# #  - Worst day
# #  - Separately and in total 
# #  Hint: 3 prints in total

# sales_w1 = [7, 3, 42, 19, 15, 35, 9]
# sales_w2 = [12, 4, 26, 10, 7, 28]

# sales = []

# sales_w2.append(int(input('Enter lemonade for the new day in week 2: ')))

# sales = sales_w1 + sales_w2

# best_day = max(sales)
# best_day_profit = best_day * 1.5
# print(f'Best day: {best_day} lemonades, Earnings: ${best_day_profit:.2f}')

# worst_day = min(sales)
# worst_day_profit = worst_day * 1.5
# print(f'Worst day: {worst_day} lemonades, Earnings: ${worst_day_profit:.2f}')


# combined_profit = best_day_profit + worst_day_profit
# print(f'Combined profit is: {combined_profit}')


# # 9.)

# csv = 'Eric, John, Michael, Terry, Graham:TerryG;Brian'

# friends_list = ['Exercise: fill me with names']

# print('Friends List:', friends_list)

# # From the list above fill a list (frined_list) properly
# # with the names of all the frineds. Ine per "slot"
# # you may need to tun same comand several times
# # use print() statements to work your way through the exercise

# csv = csv.replace(';', ', ')
# csv = csv.replace(':', ', ')


# friends_list = []
# print('Names, ', csv)
# friends_list = csv.split(',')
# print('Friends List:', friends_list)


# # 10)
# # Sets

# # 1. Check if Eric and John exist in frineds
# # 2. Combine or add the  two sets
# # 3. Find names that are in both sets
# # 4. Find names that are only in frineds
# # 5. Show only the names who only appear in one of the lists
# # 6. Create a new cars-list withouth duplicates

# friends ={'John', 'Michael', 'Terry', 'Graham', 'Eric'}
# my_frineds = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
# cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']


# # 1. Check if Eric and John exist in frineds
# print('Check if Eric and John are in friends: ', 'Eric' in friends and 'John' in friends)

# # 2. Combine or add the two sets
# all_friends = friends.union(my_frineds)
# print('All Friends:', all_friends)

# # 3. Find names that are in both sets
# common_friends = friends.intersection(my_frineds)
# print('Common friends: ', common_friends)

# # 4. Find names that are only in frineds
# names_only_in_frineds = friends.difference(my_frineds)
# print('Names only in friends set: ', names_only_in_frineds)

# # 5. Show only the names who only appear in one of the lists
# unique_friends = friends.symmetric_difference(my_frineds)
# print('Names only in one of the sets: ', unique_friends)


# # 6. Create a new cars-list withouth duplicates
# cars_set = list(set(cars))
# print('Cars list without duplicates: ', cars_set)


# # Functions
# print('Functions')

# #Add new print statement - on new line 
# # which says 'We hear you like the color xxx! xxx is a string with a color
# #2. Extend the function with another input parameter 'color', the defaults to 'red'
# #3. Capture the color via an input box as variable: color
# #4. Change the' You are xx!' text to say 'you will be xx+1 years old next birthday!'
# #5. Capitalize first letter of 'name', and rest are small caps
# #6. Favorite color should be lowercase

# def greeting(name, age=28, color='red'):
#     print(f'Hello, {name.capitalize()}!')
#     print(f'You will be {age + 1} years old next birthday!')
#     print(f'We hear you like the color {color.lower()}!')

# user_name = input('Enter your name: ')
# user_age = int(input('Enter your age: '))   
# user_color = input('Enter your favorite color: ')

# greeting(name= user_name, age=user_age, color=user_color)


# 11.) Return statements

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return f"{amount}, {tax}, {total_amount}"
# price = value_added_tax(100)
# print(price, type(price))


# #12.) if elif else - Exercise

# # Create a calculator which handles +, -, *, / and outputs answer based on the mode/ operator used

# #Hint: use 3 separate inputs
# #Bonus: Extend functionality with extra mode so it alseo does celsius to fahrenheit conversion 
# #Formula is: temp in C * 9/5 + 32 = temp in F

# def calculator(num1, operator, num2 = 0):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     elif operator.lower() == 'c to f':
#         return (num1 * 9/5) + 32
#     else:
#         return "Error: Invalid operator"

# operation = input('Enter operator (+, -, *, /) or "C to F" for temperature conversion: ')
# first_number = float(input('Enter first number: '))

# if operation.lower() == 'c to f':
#     result = calculator(first_number, operation)
#     print('Result:', result)
# else:
#     second_number = float(input('Enter second number: '))
#     result = calculator(first_number, operation, second_number )
#     print('Result:', result)


# def num_days(month):
#     days = 30

#     if month in {'jan','mar','may','jul','aug','oct','dec'}:
#         days = 31
#     elif month == 'feb':
#         days = 28
#     print(f'number of days in ${month} is {days}')


# #Testiong the function
# num_days('jun')

# #optimize/shorten the code in the function
# #try to reduce the number of conditions


##13.)
# print('Gessing game') 

# #Gues the correct number in 3 guesses. If you don't get it right after 3 guesses you lose the game.
# #Give user input box: 1. To capture guesses, 
# #print(and input boxex) 1. If user wins 2. If user loses
# #Tip: (remember you won't see print statements during execution, so If you want to see prints during 
# # while loop, then print to the input box)

# number_of_guesses = 3
# correct_number = 32
# while number_of_guesses > 0:
#     input_guess = input('Enter your guess:')
#     if(int(input_guess) == correct_number):
#         print('Great! That is correct number!')
#         break
#     number_of_guesses = number_of_guesses -1
#     if number_of_guesses == 0:
#         print('Sorry, try next time!')



##14.)
# #Coffer order queue challenge

# #1. Set up two variables: one for total price, one for drink count
# #2. Start a while True loop
# #3. Ask for customer's name
# #4. If the name is "done", break the loop
# #5. Ask for their drink order
# #6. If it si "latte", add 3.50 to the total and +1 to drink count
# #   If it is "americano", add 3.00 to total and +1 to drink count
# #   If it is "espresso", add 2.50 to the total and +1 to drink count
# #7. If it is not one of those drinks, print a warning and continue
# #8. After the loop, print total number of drinks and total price



# total_price = 0
# drink_count = 0

# drink_name = input('Dear customer, what do you want to order? Latte, americano or espresso? ')

# while(True):
#     if(drink_name.lower() == 'latte'):
#         total_price = total_price + 3.50
#         drink_count = drink_count + 1
#     elif(drink_name.lower() == 'americano'):
#         total_price = total_price + 3.00
#         drink_count = drink_count + 1
#     elif(drink_name.lower() == 'espresso'):
#          total_price = total_price + 2.50
#          drink_count = drink_count + 1    
#     elif(drink_name.lower() != 'done'):
#         print('Error! We do not have that product! Please order again. Thanks!')   
#     else:
#         break
#     drink_name = input('Dear customer, what do you want to order? Latte, americano or espresso? If you want to quit, please type "DONE"')

# print(f"Total price ${total_price:2f} and total number of orders are: {drink_count}")


# #15.)
# print("For loops - Exercise")

# # - You are having a party and want to invite your frineds. 
# # - you want the print out invitations for each frined using for loop
# # - The names are in two lists , 'names' and 'names1'
# # - You also need to add two extra names to the list using an 'input' box, when you run the code
# # - Printout one invitation to each frined per line 
# # - Names should be properly capitalized

# #Example of printout
# # John Cleese! You are invited to the party on saturday. 
# # Eric Idle! YOu are invited to the party on saturday.staticmethod

# # - Hint: you may need two (for) loops to solve this exercise

# names = ['John Doe', 'Tom Tom', 'Alex Alex', 'Julie Doe']
# names1 = ['Marry Doe', 'Anna Doe', 'Monica Doe', 'Tom Doe']
# mesage = 'You are invited to the party on saturday.'

# names.extend(names1)

# for index in range(2):
#     names.append(input('Please type First and Last name for your invitation for first group!'))
 

# for name in names: 
#     print(f"{name.title()}, {mesage}")
    

# #16.)
# #Phone number formatter

# #1. Ask the user to enter a U.S phone number in ***any format***.
# #2. Use .strip() to remove any leading/trailing spaces.
# #3. Replace common separators (-, (, ), .) with spaces/
# #4. Use .split() to break into chunks, then .join() to merge the digits.
# #5. Check if the cleaned number has ***exactly 10 digits***
# #6. If yes, format it like this: (123) 456-7890
# #7. If not, print an error message: "Please enter exactly 10 digits"

# #123-456-7890
# #(123)456.7890

# number = input('Please enter yout U.S phone number: ')
# cleaned = number.strip() 

# for ch in ['-', '(', ')', '.']:
#     cleaned = cleaned.replace(ch, " ")

# parts = cleaned.split()
# digits_only = ''.join(parts)


# if len(digits_only) == 10:
#     area = digits_only[0:3]
#     mid = digits_only[3:6]
#     end = digits_only[6:]
#     formatted_phone_number = f"({area}) {mid}-{end}"
#     print("New format of number is: ", formatted_phone_number)
# else:
#     print('Please enter exactly 10 digits')


# #17.)

# #Access control scsnner challenge

# #1. Create a set of revoked badge numbers.
# # 2. Create two empty lists: "approved" and "denied".
# # 3. Start a loop to collect visitor info:
# #     - Ask for the visitor's name (or type "done" to finish).
# #     - If the name is "done", exit the loop.
# #     - Otherwise, ask for their badge number.
# #     - Check if the badge is revoked:
# #        * If revoked: add the name to "denied" and display "ACCESS DENIED".
# #        * If not: add the name to "approved" and display "ACCESS GRANTED".
# # 4. Print the final "Access Summary" for "Approved visitors" & "Denied visitors":
# #   - Sort both lists alphabetically.
# #   - Display the total number of approved and denied visitors.

# revoked_badge_numbers= {'X123', 'B789', 'Z999'}
# approved_list = []
# denied_list = [] 

# while True:
#     visitor_name = input("Please insert your name: ")

#     if visitor_name.lower() == 'done':
#         break
#     visitor_badge_number = input('Please insert your badge numbers: ').strip().upper()
#     if visitor_badge_number in revoked_badge_numbers:
#         print(f"[ACCESS DENIED] {visitor_name} - Revoked badge")
#         denied_list.append(visitor_name.title())
#     else:
#         print(f"[ACCESS APPROVED] {visitor_name} - Revoked badge")
#         approved_list.append(visitor_name.title())


# print('APPROVED VISITORS')
# for person in sorted(approved_list):
#     print(f'- {person}')

# print('DENIED VISITORS')
# for person in sorted(denied_list):
#     print(f'- {person}')
 
# print(f"Total number of denied visitors: {len(approved_list)} and total number of approved visitors: {len(denied_list)}")

# #18.)

# #Loyality points engine challenge

# #RULES:

# #Each whole dollar spent earns 3 points
# #Tiers:
# #   < 100 pts -> Bronze
# #   100 - 499 pts -> Silver
# #   >= 500 pts -> Gold

# #Steps
# #1. Define earn_points(price) -> returns points for one purchase
# #2. Define tier_label(points) -> returns Bronze / Silver / Gold
# #3. Given the hard-coded list 'purchases',
# #   loop through it, call earn_points() for each amount, 
# #   and add the result to total_points.
# #4. After the loop, call tier_label(total_points)
# #5. Print 'Loyality Summary'
# # - Total dollars spent
# # - Total points earned
# # - Final tier

# #Purchase history (3.75, 7.20)

# purchases = [12.50]

# #Returns points for one purchase (whole dolar - int is used)
# def earn_points(price):
#     return int(price) * 3

# def tier_label(points):
#     if points < 100:
#         return 'Bronze'
#     elif points >= 100 and points < 500:
#         return 'Silver'
#     else:
#         return 'Gold'
    
# total_points = 0

# #Call earn points for each amount
# for purchase in purchases:
#     points = earn_points(purchase)
#     total_points += points

# tier_label_for_purchases = tier_label(total_points)

# print("****LOYALITY SUMMARY****")
# print(f"- Total dollars spent: {sum(purchases)}")
# print(f"Total points earned: {total_points}")
# print(f"- Final tier: {tier_label_for_purchases}")


# #19.)

# #Dog Bus tracker - Challenge Steps

# #1. Start with a bus dictionary holding current passengers.
# #   - Each seat number (1, 2, 3, ...) us a key
# #   - Each value is another dioctionary with each pet's:
# #       * name
# #       * breed
# #       * pickup time
# #       * dropoff time

# current_passengers = {
#     1: {
#     "name" : "Tom", 
#     "breed": "Labrador", 
#     "pickup_time": "8.1.2026",
#     "dropoff_time":"11.1.2026 at 8PM" 
#     },
#     2: {
#     "name" : "Tom", 
#     "breed": "Labrador", 
#     "pickup_time": "8.1.2026",
#     "dropoff_time":"15.1.2026 at 8PM" 
#     },
#     3: {
#     "name" : "Merry", 
#     "breed": "Labrador", 
#     "pickup_time": "8.1.2026",
#     "dropoff_time":"11.1.2026 at 8PM" 
#     },
# }



# #2. Print a starting roster showing each pet's seat, name, and pickup time.

# for key, value in current_passengers.items():
#     print(f"Seat number No{key}. Name is {value['name']}. Pickup time is {value['pickup_time']}.")

# MAX_SEATS = 8

# #3. Add one new pet if there is  room on the bus.
# #   - Use MAX_SEATS to limit capcaity.
# #   - Dynamically assign the next seat number
# #   - Print the updated roster showing all pets after pickup.
# current_number_of_passengers= len(current_passengers)

# while current_number_of_passengers <= MAX_SEATS:
#     print('Do you want to add more passengers?')
#     name = input('If Yes, type name. If No, type DONE. ')

#     if name.lower() =='done':
#         break
#     breed = input('Enter breed: ')
#     pickup_time = input('Enter pickup time: ')
#     dropoff_time = input('Enter dropoff time: ')

#     current_number_of_passengers+=1
#     current_passengers[current_number_of_passengers] = {
#         "name": name.title(), 
#         "breed": breed, 
#         "pickup_time": pickup_time,
#         "dropoff_time":dropoff_time 
#     }

# print(f"***ALL PETS AFTER PICKUP***")
# for key, value in current_passengers.items():
#     print(f"Seat number No{key}. Name is {value['name']}. Pickup time is {value['pickup_time']}.")



# #4. Ask which pet leaves early.
# #   - Remove that pet from the bus.
# #   - Print a message saying thet've headed home.

# print('PLEASE ADVICE IF ANY OF PET LEAVES EARLY')
# name_of_pet = input('If so, please enter name of pet. If no enter DONE: ')
# index = None

# while True:

#     if name_of_pet.lower() == 'done':
#         break

#     for key, value in current_passengers.items():
#         if value['name'].lower() == name_of_pet.lower():
#             index = key
#             print('Pet was headed home! Thanks for the ride.')
#             break

#     if index != None:
#         del current_passengers[index]
#     else:
#         print('There is no pet in the bus with that name!')

#     name_of_pet = input('If so, please enter name of pet. If no enter DONE: ')


# #5. Print a final roseter listing the remaining pets and their dropoff times.

# print(f"***FINAL ROSETER OF REMAINING PETS AND THEIR DROPOFF TIMES***")
# for key, value in current_passengers.items():
#     print(f"Seat number No{key}. Name is {value['name']}. Dropoff time is {value['dropoff_time']}.")

# 20.) #Pizza BUilder - Challenge Steps

# #1. Define a pizza class that sores:
# #   - size, crust type, and a list of toppings
# #2. Add a method to add a new topping
# #3. Add a method to remove the topping if it exists
# #4. Add a method to print pizza details:
# #   - size, crust, and all toppings (or No topings yet!)
# #5. Create a pizza object, customize it, and print the summary 

# class Pizza:
#     def __init__(self, size, crust, toppings=None):
#         self.size = size
#         self.crust = crust
#         self.toppings = toppings if toppings else []
        
#     def add_topping(self, topping):
#         self.toppings.append(topping)
    
#     def remove_topping(self, topping):
#         if topping in self.toppings:
#             self.toppings.remove(topping)
#         else:
#             print(f'The value of {topping} is not on your pizza!')
    
#     def describe_pizza(self):
#         print("\n 🍕==== Your Pizza ===🍕")
#         print(f'Size: {self.size.title()}')
#         print(f'Crust: {self.crust.title()}')
#         if self.toppings:
#             print('Toppings:')
#             for topping in self.toppings:
#                 print(f'- {topping.title()}')
#         else:
#             print('No toppings added yet!')


# my_pizza = Pizza('large', 'thin')
# my_pizza.add_topping('papperoni')
# my_pizza.add_topping('onions')

# my_pizza.describe_pizza()

# my_pizza.remove_topping('ham')
# my_pizza.describe_pizza()
    

# #LAMBDA FUNCTIONS:

# f = lambda x: x + 5

# print(f(2))

# strip_spaces = lambda str: ''.join(str.split(' '))

# print(strip_spaces('Monty Pythons Flying Circus'))

# join_list_no_duplicates = lambda list_a, list_b: list(set(list_a + list_b))

# list_a = [1, 2, 3, 4]
# list_b = [3, 4, 5, 6, 7]

# print(join_list_no_duplicates(list_a, list_b))

# def create_quad_func(a, b, c):
#     # Return function f(x) = ax^2 + bx + c
#     return lambda x: a*x**2 + b*x + c

# f = create_quad_func(2, 4, 6)

# g = create_quad_func(1, 2, 3)

# print(f(2))
# print(g(2))

# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']

# print(sorted(signups))

# print(sorted(signups, key= lambda id: int(id[3:])))


# class Player:

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# Eric = Player('Eric', 1232)
# John = Player('John', 39032)
# Terry = Player('Terry', 4930)

# player_list = [Eric, John, Terry]


# player_list.sort(key= lambda player: player.score, reverse=True)
# print([player.name for player in player_list])

# import random

# print(random.random())

#Raffle Prze Picker - Challenge Steps

#1. Ask how many people are entering the raffle (at least 3 names).
#2. Use a loop to collect their names into a list.
#3. Ask for exactly 3 prize names (in order) and store them in a list.
#4. Randomly pick 3 different winners from the participant list.
#5. Print out who wins prize and make sure the final one 
# is clearly marked as the Grand Prize.

#Hint: Use loops, lists, and a tool that picks random items without repeats. 

people_number = int(input('Please enter how many people are entering the raffle? '))

if people_number < 3:
    print("You need at least 3 participants to run the raffle!")
    exit()

names = []

for i in range(people_number):
    name = input(f'Please enter #{i+1} name: ')
    names.append(name)


prizes = []

for i in range(3):
    prize = input(f'Prize #{i+1}: ')
    prizes.append(prize)

import random


winners = random.sample(names, 3)

print("Raffle results")
for i in range(3):
    if i  == 2:
        print(f"Grand prize: {winners[i].title()} wins the {prizes[i].title()}")
    else:
        print(f"{winners[i].title()} wins the {prizes[i].title()}")
    
    
