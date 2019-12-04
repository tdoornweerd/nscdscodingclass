
def translate_bi_to_word():
        bi = input('type binary here: ')
        length = len(bi)//8
        words = []
        for i in range(length):
                words.append(chr(bi_to_num(bi[i*8:(i*8)+8])))
        print(''.join(words))
        again()
def add_bi():
        new_bi = []
        carry = False
        first_bi = input('put first bianary: ')
        print('you entered: ', bi_to_num(first_bi))
        second_bi = input('put second bianary: ')
        print('you entered: ', bi_to_num(second_bi))
        first_bi = list(first_bi)
        second_bi = list(second_bi)
        if len(first_bi) >= len(second_bi):
                longer = len(first_bi)
                while len(second_bi) < len(first_bi):
                        second_bi.insert(0,'0')
        else:
                longer = len(second_bi)
                while len(first_bi) < len(second_bi):
                        first_bi.insert(0,'0')
        for i in range(longer):
                place = (longer - 1) - i
                if first_bi[place] == '1' and second_bi[place] == '1':
                        if carry == True:
                                new_bi.insert(0,'1')
                        elif carry == False:
                                new_bi.insert(0,'0')
                                carry = True
                elif first_bi[place] != second_bi[place]:
                        if carry == True:
                                new_bi.insert(0,'0')
                        elif carry == False:
                                new_bi.insert(0,'1')
                elif first_bi[place] == '0' and second_bi[place] == '0':
                        if carry == False:
                                new_bi.insert(0,'0')
                        if carry == True:
                                new_bi.insert(0,'1')
                                carry = False
        if carry == True:
                new_bi.insert(0,'1')
        elif carry == False:
                None
        print('the answer is',''.join(new_bi),' in bianary or', bi_to_num(''.join(new_bi)),'in decimal')
        again()
def bi_to_num(bianary):
        number = 0
        bianary = list(bianary)
        for i in range(len(bianary)):
                if bianary[i] == '1':
                        number += 2**((len(bianary)-1)-i)
        return number
def bi_to_num_full():
        bianary = input('put bianary here: ')
        print(bi_to_num(bianary))
        again()        
def num_to_bi():
        number = []
        i = 0
        bi = []
        running = []
        number = input('put the number here: ')
        number = int(number)
        running.append(number)
        while 2**i < number:
                i+=1
        for f in reversed(range(i)):
                if 2**f < running[-1] or 2**f == running[-1]:
                        bi.append('1')
                        running.append(running[-1] - 2**f)
                else:
                        bi.append('0')
        print(''.join(bi))
        again()
def again():
        again1 = input('press 1 to go again and 2 to quite')
        if again1 == '1':
                finder()
        elif again1 =='2':
                print('bye')                        
def finder():
        choice = input('If bianary to num press 1 enter. If num to bianary press 2 enter. If bianary addition press 3 enter. If translate bianary to word press 4 enter.')
        if choice == '1':
                bi_to_num_full()
        elif choice == '2':
                num_to_bi()
        elif choice == '3':
                add_bi()
        elif choice == '4':
                translate_bi_to_word()
finder()