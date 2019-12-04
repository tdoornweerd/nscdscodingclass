import random

word_file = "words for password.txt"
word_list = []
final_list = []

with open(word_file,'r') as words:
	for line in words:
		word = line.strip().lower()
		if 3 < len(word) < 8:
			word_list.append(word)

def genrando():
	r = random.randint(1,len(word_list)-1)
	jjj = word_list[r]
	final_list.append(jjj)
	
def generate_password():
	for i in range(3):
		genrando()
	dapass = ''.join(final_list)
	dapass.lower()
	print(dapass)
	final_list.clear()

generate_password()