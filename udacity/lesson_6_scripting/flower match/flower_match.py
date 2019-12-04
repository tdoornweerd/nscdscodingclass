match = {}
with open('flowers.txt','r') as f:
    read = f.read().splitlines()
for pair in read:
    pair = pair.split(': ')
    match.update({pair[0]:pair[1]})
names = input('enter name: ')
print('Unique flower name with the first letter: {}'.format(match.get(names[0])))