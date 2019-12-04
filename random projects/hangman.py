import random
def again():
        again1 = input('press 1 to go again and 2 to quite')
        if again1 == '1':
                finder()
        elif again1 =='2':
                print('bye')
                exit()
def two_player_unlimited():
    word = input('player 1 input the word that player two needs to guess: ')
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_used = []
    word = list(word)
    blank = ''
    for i in range(20):
        print('')
    for i in range(len(word)):
        blank = blank + '_'

    word_right = False
    wrong_guesses = 0
    while wrong_guesses < 6:
        for l in range(20):
            print('')
        guess = input('guess letter:')
        if guess not in alphabet:
            print("either this isn't a letter or you already used this letter. Try again")


        elif guess in alphabet:
            for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        alphabet.remove(alphabet[i])
                        break
            
            
            if guess in word:
                blank = list(blank)
                for i in range(len(word)):
                    if guess == word[i]:
                        blank[i] = guess


            
            
            else:
                wrong_guesses+= 1
                print('no not in word')
                for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        letters_used.extend(alphabet[i])
                        print(letters_used)
                        alphabet.remove(alphabet[i])
                        print(''.join(letters_used),'!!!!!!!!!!!!!!')
                        break
            


        print(' '.join(blank))    
        print('letters you have left',' '.join(alphabet))


        print(letters_used)
           

        if ''.join(blank) == ''.join(word):
            print('youuuuuuuu winnnnnnnn!!!!')
            print('your score: ', wrong_guesses)
            word_right = True
            again()
def two_player_classic():
    word = input('player 1 input the word that player two needs to guess: ')
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_used = []
    word = list(word)
    blank = ''
    for i in range(20):
        print('')
    for i in range(len(word)):
        blank = blank + '_'


    wrong_guesses = 0
    while wrong_guesses < 6:
        for l in range(20):
            print('')
        guess = input('guess letter:')
        if guess not in alphabet:
            print("either this isn't a letter or you already used this letter. Try again")


        elif guess in alphabet:
            for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        alphabet.remove(alphabet[i])
                        break
            
            
            if guess in word:
                blank = list(blank)
                for i in range(len(word)):
                    if guess == word[i]:
                        blank[i] = guess


            
            
            else:
                wrong_guesses+= 1
                print('no not in word')
                for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        letters_used.extend(alphabet[i])
                        print(letters_used)
                        alphabet.remove(alphabet[i])
                        print(''.join(letters_used),'!!!!!!!!!!!!!!')
                        break
            


        print(' '.join(blank))    
        print('letters you have left',' '.join(alphabet))
        
        if wrong_guesses > 0:
            print('stickman:')
            if wrong_guesses == 5:
                print('head, body, right arm, left arm, right leg')
            elif wrong_guesses == 4:
                print('head, body, right arm, left arm')
            elif wrong_guesses == 3:
                print('head, body, right arm')
            elif wrong_guesses == 2:
                print('head, body')
            elif wrong_guesses == 1:
                print('head')


        print(letters_used)
           

        if ''.join(blank) == ''.join(word):
            print('youuuuuuuu winnnnnnnn!!!!')
            again()
def vs_comp_classic():
    word = ""
    word_file = "theword.txt"
    with open(word_file,'r') as f:
        words = f.read()
    words = words.split()
    list(words)
    r = random.randint(1,len(words)-1)
    
    word = words[r]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_used = []
    word = list(word)
    blank = ''
    for i in range(20):
        print('')
    for i in range(len(word)):
        blank = blank + '_'


    wrong_guesses = 0
    while wrong_guesses < 6:
        for i in range(20):
            print('')
        guess = input('guess letter:')
        if guess not in alphabet:
            print("either this isn't a letter or you already used this letter. Try again")


        elif guess in alphabet:
            for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        alphabet.remove(alphabet[i])
                        break
            
            
            if guess in word:
                blank = list(blank)
                for i in range(len(word)):
                    if guess == word[i]:
                        blank[i] = guess


            
            
            else:
                wrong_guesses+= 1
                print('no not in word')
                for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        letters_used.extend(alphabet[i])
                        print(letters_used)
                        alphabet.remove(alphabet[i])
                        print(''.join(letters_used),'!!!!!!!!!!!!!!')
                        break
            


        print(' '.join(blank))    
        print('letters you have left',' '.join(alphabet))
        
        if wrong_guesses > 0:
            print('stickman:')
            if wrong_guesses == 6:
                print('head, body, right arm, left arm, right leg, left leg')
                print('you lose... the word was:',''.join(word))
            elif wrong_guesses == 5:
                print('head, body, right arm, left arm, right leg')
            elif wrong_guesses == 4:
                print('head, body, right arm, left arm')
            elif wrong_guesses == 3:
                print('head, body, right arm')
            elif wrong_guesses == 2:
                print('head, body')
            elif wrong_guesses == 1:
                print('head')
            


        print(letters_used)
        #if letters_used:
        #    print('letters that were wrong')#,' '.join(letters_used))        

        if ''.join(blank) == ''.join(word):
            print('youuuuuuuu winnnnnnnn!!!!')
            again()
def vs_comp_unlimited():
    word = ""
    word_file = "theword.txt"
    with open(word_file,'r') as f:
        words = f.read()
    words = words.split()
    list(words)
    r = random.randint(1,len(words)-1)
    
    word = words[r]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_used = []
    word = list(word)
    blank = ''
    for i in range(20):
        print('')
    for i in range(len(word)):
        blank = blank + '_'

    word_right = False
    wrong_guesses = 0
    while word_right == False:
        for i in range(20):
            print('')
        guess = input('guess letter:')
        if guess not in alphabet:
            print("either this isn't a letter or you already used this letter. Try again")
        elif guess in alphabet:
            for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        alphabet.remove(alphabet[i])
                        break
            
            
            if guess in word:
                blank = list(blank)
                for i in range(len(word)):
                    if guess == word[i]:
                        blank[i] = guess


            
            
            else:
                wrong_guesses+= 1
                print('no not in word')
                for i in range(len(alphabet)):
                    if guess == alphabet[i]:
                        letters_used.extend(alphabet[i])
                        print(letters_used)
                        alphabet.remove(alphabet[i])
                        print(''.join(letters_used),'!!!!!!!!!!!!!!')
                        break
        print(' '.join(blank))    
        print('letters you have left',' '.join(alphabet))

        print(letters_used)
        #if letters_used:
        #    print('letters that were wrong')#,' '.join(letters_used))        

        if ''.join(blank) == ''.join(word):
            print('youuuuuuuu winnnnnnnn!!!!')
            print('your score is ', wrong_guesses)
            word_right = True
            again()
def finder():
    mode = input("type 2 for two player. Type 1 for one player: ")
    if mode == "2":
        mode3 = input('unlimited guesses? press 1 for yes and 2 for no: ')
        if mode3 == '1':
            two_player_unlimited()
        elif mode3 == '2':
            two_player_classic()
    elif mode == '1':
        mode2 = input('unlimited guesses? press 1 for yes and 2 for no: ')
        if mode2 == '1':
            vs_comp_unlimited()
        elif mode2 == '2':
            vs_comp_classic()

finder()
