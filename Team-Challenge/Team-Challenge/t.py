data = [1,0,1,0,1000]

def ispallydrone(word):
    lista = list(word)
    listb = list(reversed(word))
    if lista == listb:
        print('true')
    else:
        print('false')


def biggest(intigers):
    intigers = list(intigers)
    big = 0
    for i in range(len(intigers)-1):
        num = intigers[i] * intigers[i + 1]
        if num>=big:
            big = num
    print(big)


biggest(data)