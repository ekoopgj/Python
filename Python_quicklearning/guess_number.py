import random

sum=0
number = random.randint(1,20)
print("I am think of a number between 1 and 20")
print("You have 4 chances!")
for i in range(5):

	guess_n = int(input("Take a guess\n"))
	sum += 1
	if i == 4:
		print("Game over!")
	elif guess_n < number:
		print ("your guess is too low" )
	elif guess_n > number:
		print ("your guess is too high")
	elif guess_n == number:
		print ("Good job! your guessed my number is " + str(sum) + " guesses")
		break