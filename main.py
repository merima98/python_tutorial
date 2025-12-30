# Arcade Day Pass Tracker - Challlenge Steps

# 1) Create variables to store:
#  - customer name
#  - number of passes
#  - tokens per pass
#  - price per pass
#  - tokens required per game

customer_name = "Alice"
number_of_passes = 3
tokens_per_pass = 50
price_per_pass = 20.0
tokens_per_game = 15



# 2) Calculate:
#  - total tokens
total_tokens = number_of_passes * tokens_per_pass
#  - total cost
total_cost = number_of_passes * price_per_pass
#  - games available (use 'floor division' to get a whole number)
games_available = total_tokens // tokens_per_game

# 3) Print a summary with :
#  - customer name
#  - passes bought
#  - total tokens
#  - total cost
#  - games available

print('Customer Name:', customer_name)
print('Passes Bought:', number_of_passes)
print('Total Tokens:', total_tokens)
print('Total Cost:', total_cost)
print('Games Available:', games_available)
