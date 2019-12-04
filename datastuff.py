
import unicodecsv

def make_list_of_csv(csv_file):
    with open(csv_file,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = make_list_of_csv('enrollments.csv')
daily_engagement = make_list_of_csv('daily_engagement.csv')
project_submissions = make_list_of_csv('project_submissions.csv')

for i in range(len(daily_engagement)):
    daily_engagement[i]['account_key'] = daily_engagement[i]['acct']
    del daily_engagement[i]['acct']

#print(enrollments[0])
#print(daily_engagement[0])
#print(project_submissions[0])

######################################################################################################################################
from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['join_date'] = parse_date(enrollment['join_date'])

#######################################################################################################################################################
def unique_student_finder(logs):
    unique_student_list = set()
    for i in range(len(logs)):
        curr_enroll = logs[i]['account_key']
        unique_student_list.add(curr_enroll)
    return unique_student_list

list_of_enrolled = unique_student_finder(enrollments)
#print('total enroll', len(list_of_enrolled))

list_of_total_daily = unique_student_finder(daily_engagement)
#print('uneque daily:', len(list_of_total_daily))

list_project_submissions = unique_student_finder(project_submissions)
#print('uneque project sub:', len(list_project_submissions))

##########################################################################################################################################################

not_in_total_daily = []
for i in list_of_enrolled:
    if i not in list_of_total_daily:
        not_in_total_daily.append(i)
#print(not_in_total_daily)

def print_if_not_in_total_daily(num):
    for i in range(len(enrollments)):
        if enrollments[i]['account_key'] == not_in_total_daily[num]:
            print(enrollments[i])
#print(print_if_not_in_total_daily(1),print_if_not_in_total_daily(2),print_if_not_in_total_daily(46))

########################################################################################################################################################
test_accounts = set()

for i in range(len(enrollments)):
    if enrollments[i]['is_udacity'] == 'True':
        test_accounts.add(enrollments[i]['account_key'])
print(test_accounts)


def take_out_udacity(data):
    only_students = []
    for student in range(len(data)):
        if data[student]['account_key'] not in test_accounts:
            only_students.append(data[student])
    return only_students


non_udacity_enrollments = take_out_udacity(enrollments)
print(len(non_udacity_enrollments))
non_udacity_engagement = take_out_udacity(daily_engagement)
print(len(non_udacity_engagement))
non_udacity_submissions = take_out_udacity(project_submissions)
print(len(non_udacity_submissions))

LESSON 14######################################################################################################################################################
print("hello world")

print('i hope this works')
