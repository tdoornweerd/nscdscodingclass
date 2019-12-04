list1 = ['one','two','three','four','five','six']
list2 = [1,2,3,4,5,6]

dictionary1 = dict()

for i in range(len(list1)):
    dictionary1[list1[i]] = list2[i]

print(dictionary1)