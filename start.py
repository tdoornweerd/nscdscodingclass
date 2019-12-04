import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

with open('daily_engagement.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)
    
with open('project_submissions.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)

#####################################################################################################################################################
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
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
#####################################################################################################################################################
# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date']) #got rid of parse_date bc didnt work??
#####################################################################################################################################################
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])
#####################################################################################################################################################
#total # of entries
#print(len(enrollments))
#print(len(daily_engagement))
#print(len(project_submissions))
#####################################################################################################################################################
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del engagement_record['acct']
#####################################################################################################################################################
def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

unique_enrolled_students = get_unique_students(enrollments)
unique_engagement_students  = get_unique_students(daily_engagement)
unique_project_submitters  = get_unique_students(project_submissions)

#print(len(unique_enrolled_students))
#print(len(unique_engagement_students))
#print(len(unique_project_submitters))
#####################################################################################################################################################
#numbers of accounts that are test accounts
def find_test(accounts):
    test_accounts = []
    test_account_number = []
    for account in accounts:
        if account['is_udacity'] == True:
            test_accounts.append(account)
        for acct in test_accounts:
            test_account_number.append(acct['account_key'])
    return test_account_number
test_account_number = find_test(enrollments)
#####################################################################################################################################################
def rid_of_test(accounts):
    non_test_account = []
    for account in accounts:
        if account['account_key'] not in test_account_number:
            non_test_account.append(account)
    return non_test_account

non_udacity_enrollments = rid_of_test(enrollments)
non_udacity_engagement = rid_of_test(daily_engagement)
non_udacity_submissions = rid_of_test(project_submissions)

#print(non_udacity_enrollments[7])
#print(non_udacity_enrollments[78])
#print(non_udacity_enrollments[67])
#####################################################################################################################################################
paid_students = {}
for students in non_udacity_enrollments:
    if students['days_to_cancel'] == None or students['days_to_cancel'] > 7:
        account = students['account_key']
        enroll_date = students['join_date']
        if account not in paid_students or enroll_date > paid_students[account]:
            paid_students.update( {account : enroll_date} )
#print(len(paid_students))
#####################################################################################################################################################
# Takes a student's join date and the date of a specific engagement record,
# and returns True if that engagement record happened within one week
# of the student joining.
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7
#####################################################################################################################################################
paid_engagement_in_first_week = []

for data in non_udacity_engagement:
    if data['account_key'] in paid_students:
        engagement_date = data['utc_date']
        join_date = paid_students[data['account_key']]
        if within_one_week(join_date,engagement_date) == True:
            paid_engagement_in_first_week.append(data)
#print(paid_engagement_in_first_week[78])

#####################################################################################################################################################
#make dic of account keys matched with lists of engagement record in first week
from collections import defaultdict

acerage = []

engagement_by_account = defaultdict(list)
for account in paid_engagement_in_first_week:
    engagement_by_account[account['account_key']].append(account)

for i in engagement_by_account:
    acerage.append(int(i))
print(sum(acerage)/len(acerage))

#time_spend_in_first_week = []
#for account in engagement_by_account:
 #   for time in account:


        #time_spend_in_first_week.append(time['total_minutes_visited'])
#print(time_spend_in_first_week)