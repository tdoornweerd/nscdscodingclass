names = input('enter names seperated by commas: ').split(',')
assignments = input('Enter assignment counts separated by commas: ').split(',')
grades =  input('Enter grade counts separated by commas: ').split(',')

message = "Hi {},\nThis is a reminder that you have {} assignments left to submit before you can graduate. \n You're current grade is {} and can increase to {} if you submit all assignments before the due date."

i=0
for name in names:
    print(message.format(names[i],assignments[i],grades[i],int(grades[i])+int(assignments[i])*2))
    i+=1