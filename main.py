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