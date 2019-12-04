with open('testy.txt', 'w') as f:
    f.write("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo there!")


with open('testy.txt','r') as c:
    readed = c.read()

print(readed)