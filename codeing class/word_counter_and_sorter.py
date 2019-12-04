word_counter = dict()
vowel_counter = dict()
consonant_counter = dict()
vowels = ['a','e','i','o','u']
words = input('put the text here: ')
delete = ['.',',','?','!',"'s",'"',"'",'@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','[',']']
for charicter in delete:
    if charicter in words:
        words = words.replace(charicter,'')
for letter in words:
    word = words.lower()
print(word)
for letter in word:
    if letter == ' ':
        None
    elif letter in vowel_counter:
        vowel_counter[letter] += 1
    elif letter in consonant_counter:
        consonant_counter[letter] += 1
    elif letter in vowels:
        vowel_counter.update({letter : 1})
    else:
        consonant_counter.update({letter : 1})
word = word.split(' ')
for word in word:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter.update({word : 1})
print( )
print('there were',sum(vowel_counter.values()) +  sum(consonant_counter.values()), 'total characters: ')
print('there were', sum(word_counter.values()), ' total words. There are ',len(word_counter), 'uneque words. Here they are with the number of times they appear: ', word_counter) 
print('there were', sum(vowel_counter.values()), 'vowels. Here they are with the number of times they appear:', vowel_counter)
print('there were', sum(consonant_counter.values()), 'consonants.')