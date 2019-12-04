def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list

cast_list = create_cast_list('list of names for lesson 6.txt')
for actor in cast_list:
    print(actor)