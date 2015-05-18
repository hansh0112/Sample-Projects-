import random

f=open('C:\Python34\state-capitals.txt','r')
h=open('C:\Python34\hangman.txt','r')

first_input = input("Please type 1 to play states-capitals game, type 2 to play hangman! :")

if first_input == '1':
	lines=f.readlines()

	states=[splitted.split(',')[0] for splitted in lines]
	capitals =[splitted.split(',')[1] for splitted in lines]
	states_list = [lowercase.lower() for lowercase in capitals]
	states_list = [realvalue.rstrip("\n") for realvalue in states_list]

	while True: 
		print("Please enter the capital cities of the state. Type 'exit' to stop playing")

		random_state = random.randint(0,len(states)-1)
		user_input = input("{}: ".format(states[random_state])) 

		user_input = user_input.lower() 

		if user_input == states_list[random_state]:
			print("Correct! Try the next one!")
		elif user_input == 'exit':
			break
		else:
			print("Please try again")
			print("The answer was {}".format(capitals[random_state]))

if first_input == '2':
	hangman_lines = h.readlines()

	hangman_lines = [nospace.rstrip("\n") for nospace in hangman_lines]

	

	random_state = random.randint(0,len(hangman_lines)-1)


	hangman_input = input("Please guess a letter. Type 'exit' to stop playing: ")
	while hangman_input != "exit":
		if len(hangman_input) > 1:
			hangman_input = input("Please guess a letter. Type 'exit' to stop playing: ")
		else: 
			break 
		

	random_word = hangman_lines[random_state]
	x = 0 
	y = 0 
	p = 0 
	word = []
	z = len(random_word) + 2 
	while x < z: 

		if hangman_input == "exit":
			break 
		print("You have {} chances left!".format(z - x))  
		while y < len(random_word):
			word.append("X")
			y = y + 1
		while p < len(random_word): 
			if random_word[p] == hangman_input:
				word[p] = hangman_input 
				p = p + 1 
			else:
				p = p+ 1 
		if p == len(random_word):
			print("{}".format(word)) 
		if "X" not in word:
			print("Congratulations! you have successfully guessed the word")
			print("")
			break 
		p = 0 
		x = x + 1 
		hangman_input = input("Please guess a letter. Type 'exit' to stop playing: ")
		while hangman_input != "exit":
			if len(hangman_input) > 1:
				hangman_input = input("Please guess a letter. Type 'exit' to stop playing: ")
			else: 
				break 
			
		
	if x == z:
		if "X" not in word:
			print("Congratulations! you have successfully guessed the word")
			print("")
		else:
			print("No more chances left! The word was {}".format(random_word))

			
				
					


