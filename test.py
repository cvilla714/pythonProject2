def replace(list,target,swap_value):
    for i in range(len(list)):
        if list[i] == target:
            list[i] = swap_value
    return list

print(replace([1,2,3,4,5,3,7,3],3,0))
print(replace(["time","flies","like","an","arrow","like","it","is","too","like"],"like","love"))
print(replace(["time","hello","great"],"hello","is"))


import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.

# this is how we start we have to ask the user for a number
start = input('Enter the start of the range: ')
# the reason why we use a whie loop is because we want to keep asking the user for a number until they enter a valid one
while not start.isdigit():
    print('Please enter a valid number.')
    # once we know the user is not providing a valid number we can ask them for a new number
    start = input('Enter the start of the range: ')
# we apply the same thing for the second number
end = input('Enter the end of the range: ')
while not end.isdigit() or int(end) < int(start):
    print('Please enter a valid number.')
    end = input('Enter the end of the range: ')

# here we are using the random module to pick a random number between the two numbers we provided
random_number = random.randint(int(start), int(end))
# i am starting the value of guess at None because that way the while loop will run at least once
guess = None
# this will keep track of how many times the user has guessed
attempts = 0

# here is where the loop starts
while guess != random_number:
    guessed_number = input("Guess a number: ")
    if not guessed_number.isdigit():
        print("Please enter a valid number.")
        continue

    attempts += 1
    guess = int(guessed_number)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f'You guessed the number in {attempts} attempt{suffix}')