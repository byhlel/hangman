from random_word import RandomWords

def rule():
	print("Here are the rules of the Hangman:")
	print("The objective of the game is to guess the word before you get Hangman!")
	print("You have 6, 9 or 12 lives to figure out the word randomly chosen")
	print("You can also choose between 3 maximum sizes for the words: 6, 8 or any")
	print("For each guess you can either try for a letter a the whole word")
	print("If you get a wrong letter, you will loose a life")
	print("If you get a wrong word, you will loose two lifes")
	print("In order to win you must guess all letters (hence the word) before you ran out of lives")
	print("Otherwise you loose i.e. I win :satisfied:")
	print("Enjoy!!\n")

def hangman():
	print("Welcome to the Hangman game made by byhlel")
	
	rules = input("Do you want to know the rules of the game? Types y (yes) or n (no)\n")
	while rules!="y" and rules!="yes" and rules!="n" and rules!="no":
		rules = input("Please enter a correct answer. \nDo you want to know the rules of the game? Types y (yes) or n (no)\n")
	if rules=="yes" or rules =="y":
		rule()

	def lives():
		lives=input("How many lives do you want ? \nRecommended 6,9 or 12 (anything above 12 will not be accepted)\n")
		while not lives.isdigit() :
			lives=input("How many lives do you want ? \nRecommended 6,9 or 12 (anything above 12 will not be accepted)\n")
		return int(lives)
	live=lives()
	while live>12:
		live=lives()
	
	level=input("What level do you want to play?\n\t0/Easy: At most 6 letters word\n\t1/Medium: At most 8 letters words\n\t2/Difficult: Any size\n")
	while level!="0" and level!="1"and level!="2":
		level=input("What level do you want to play?\n\t0/Easy: At most 6 letters word\n\t1/Medium: At most 8 letters words\n\t2/Difficult: Any size\n")
	maxlen=15
	if level=="0":
		maxlen=6
	elif level=="1":
		maxlen=6

	r=RandomWords()
	word=r.get_random_word(hasDictionaryDef="true",maxLength=maxlen)
	while word==None:#This is to prevent an issue caused by dictionnary at time of coding
		word=r.get_random_word(hasDictionaryDef="true",maxLength=maxlen)
	word_print=list(word)
	result=list(word)
	used_letters=[]
	while "-" in result:
		result[result.index("-")]="?"

	while not all(elem == "?" for elem in result) and live!=0:
		letter=input("Enter a letter or a word\n")
		print()
		if len(letter)==1:
			if letter<'a' or letter >'z':
				print("Not a letter")
			elif letter in used_letters:
				print("You have already tried that letter")
			elif letter in result:
				used_letters.append(letter)
				while letter in result:
					result[result.index(letter)]="?"
				print("Letter: "+letter+ " in word")
			else:
				used_letters.append(letter)
				print("Letter: "+letter+ " not in word")
				live-=1
		else:
			i=0
			while i<len(letter) and letter[i]>='a' and letter[i]<='z':
				i+=1
			corect= i==len(letter)
			if not correct:
				print("Not a word")
			elif letter!=word:
				live-=2
				print("Wrong word")
			else:
				break
		for i in range(len(result)):
			if result[i]!="?":
				print("_",end=" ")
			else:
				print(word_print[i],end=" ")
		print(f"\nYou have {live} lives left")
		for i in range(live):
			print(u'\u2764',end="")
		print("\nHere are your used letters: ",used_letters,end="\n\n")
	if live>0:
		print("You have won, the word was : "+ word+"\n")
	else:
		print("You have lost, the word was : "+ word+"\n")
	exit=input("Do you want to play again? If no press Enter to exit or anything else to play again\n")
	if exit!="":
		print("\n")
		hangman()

hangman()
