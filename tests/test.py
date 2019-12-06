list1 = ['one','two','three','four','five','six']
list2 = [1,2,3,4,5,6]

dictionary1 = dict()

for i in range(len(list1)):
    dictionary1[list1[i]] = list2[i]

print(dictionary1)


def take_out_free(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = take_out_free(non_udacity_enrollments)
paid_engagement = take_out_free(non_udacity_engagement)
paid_submissions = take_out_free(non_udacity_submissions)