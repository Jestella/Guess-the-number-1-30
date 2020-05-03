import random
number = random.randint(1,30)
player_name = input("Welcome, your name?")
number_of_guesses = 0
print('okay! '+ player_name+ '! Guess a number between 1 and 30: ')

while number_of_guesses < 8:
  guess = int(input())
  number_of_guesses += 1
  if guess < number:
    print('Your guess is too low')
  if guess > number:
    print('Your guess is too high')
  if guess == number:
    break

if guess == number:
  print('Congrats! You guessed the number in '+ str(number_of_guesses) + ' tries!')
else:
  print('You did not guess the number, The number was ' + str(number))

