
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
for engement in daily_engagement:
    engement['utc_date'] = parse_date(engement['utc_date'])

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
#print(test_accounts)


def take_out_udacity(data):
    only_students = []
    for student in range(len(data)):
        if data[student]['account_key'] not in test_accounts:
            only_students.append(data[student])
    return only_students


non_udacity_enrollments = take_out_udacity(enrollments)
#print(len(non_udacity_enrollments))
non_udacity_engagement = take_out_udacity(daily_engagement)
#print(len(non_udacity_engagement))
non_udacity_submissions = take_out_udacity(project_submissions)
#print(len(non_udacity_submissions))

#LESSON 14######################################################################################################################################################
#only look at students engement from the first week and dont look at students who quit after a week
#create dictionary of students who havent cancelled (days to cancell = none) and stayed enrolled for more than 7 days (days to cancell = >7)
#key = account key and value = enrollment date|| dic name = paid students 
#only add if most recent or if new

paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or enrollment['days_to_cancel'] == None or enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date


#print(len(paid_students))



def remove_free_trial_cancel(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancel(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancel(non_udacity_engagement)
paid_submissions = remove_free_trial_cancel(non_udacity_submissions)

def find_account_key(data_set,key):
    if key in data_set:
        return key

paid_engagement_in_first_week = []
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

for engagement in paid_engagement:
    engagement_date = engagement['utc_date']
    account_key = engagement['account_key']
    join_date = find_account_key(paid_students,account_key)
    print(engagement,)
    if account_key in paid_students and within_one_week(join_date,engagement_date) == True:
        paid_engagement_in_first_week.append(engagement)

print(len(paid_engagement_in_first_week))
