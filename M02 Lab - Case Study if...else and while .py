"""
Payden Schug
M02 Lab - Case Study if...else and while .py
This app allows the user to enter a students last name, first name, and GPA. It will then determine if they have made any applicable list corresponding to their GPA. Additionally, this app includes
a small demonstration of 5 different complete student inputs to help the user understand what they are accomplishing.
last updated 11/5/2023
"""

#declaring lists for example block
firstNameList = ['jack', 'guy', 'sarah', 'hannah', 'james', 'null']
lastNameList =  ['jameson', 'fieri', 'connor', 'bobana', 'dean', 'AAA']
gradePointAverageList = [3.57, 2.21, 4.00, 3.26, 3.24, 0]

#declaring variables
firstName = 'john'
lastName = 'doe'
gradePointAverage = float(0.00)

#main body
while lastName != 'ZZZ':
    #allowing user to choose between inputting their own students or seeing an example demonstration
    customOrExample = input("To enter students names, enter C. To see an example of 5 students, enter E. \n")

 #custom input body
    if customOrExample == 'c':
        #infinite loop to allow for user to continously enter data until they enter the sentinel value
        while 1 == 1:
            
            lastName = input("Enter the student's last name, or enter ZZZ to quit. \n") #last name input
            if lastName == 'ZZZ': #check for sentinel, exiting if found
                break
            firstName = input("Enter the student's first name \n") #first name input
            gradePointAverage = float(input("Enter the student's GPA \n")) #GPA input

            if gradePointAverage >= 3.5: #checking for deans list threshold
                print(firstName, lastName, "has made the Deans List.")
            elif gradePointAverage >= 3.25: #checking for honor roll threshold
                print(firstName, lastName, "has made the Honor Roll")
            else: #declaring that neither list's requirements were met
                print(firsName, lastName, "has not made any list")

 #demonstration body
    elif customOrExample == 'E':
        #largely the same as the custom input, but instead the pre-declared parallel lists are iterated and used as the 'input', with the running values printed at every step for user demonstration.
        print ("This program allows you to enter a student's last name, first name, and GPA. It will then determine if they have made either the Dean's List or the Honor Roll. In this demonstration, the entered demonstration info will be shown to you.")
        i = 0 #iterator
        while 1 == 1:
            
            lastName = lastNameList[i]
            if lastName == 'AAA': #changed ZZZ to AAA so that the demonstration exits without exiting the program.
                break
            print("The last name entered was", lastName, "\n")
            firstName = firstNameList[i]
            print("The first name entered was", firstName, "\n")
            gradePointAverage = gradePointAverageList[i]
            print("The GPA entered was", gradePointAverage, "\n")
            if gradePointAverage >= 3.5:
                print(firstName, lastName, "has made the Deans List. \n")
                i = i + 1
            elif gradePointAverage >= 3.25:
                print(firstName, lastName, "has made the Honor Roll \n")
                i = i + 1
            else:
                print(firstName, lastName, "has not made any list \n")
                i = i + 1
        