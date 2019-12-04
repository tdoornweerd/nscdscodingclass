students = set([1,2,3,4,5])
the_list = [7,8,5,9,10,1,1,1,1]
newandbetter_list = []

for i in range(len(the_list)):
    if the_list[i] not in students:
        newandbetter_list.append(the_list[i])

print(the_list)
print(newandbetter_list)