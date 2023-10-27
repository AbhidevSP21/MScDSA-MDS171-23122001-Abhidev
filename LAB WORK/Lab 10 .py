# Create a Python Class for managing student details and marks.
# Define the class and implement the methods of the student class in a menu-driven program for different types of users

class classroom:

    def _init_(self):
        self.classroom = {
            'Students' : []
        }

    def collectinfo(self,roll,name,subject,mark):
        self.info = {
            roll : {
                'Name' : name,
                'Subject' : subject,
                'Mark' : mark
            }
        }

        self.classroom['Students'].append(self.info)
        print(self.classroom)

    def view(self):
        print(self.classroom)

    def update(self):
        print('1. Name')
        print('2. Subject')
        print('3. Marks')

        while True:

            choice_1 = int(input('Enter what value is to be updated: '))
        
            if choice_1 == 1:
                ask_name = input('Enter the name to be changed: ')
                ask_roll = input("Enter that student's roll: ")
                new_name = input("Enter the new name to be stored: ")
                self.classroom[ask_roll][ask_name] = new_name
                print(self.classroom)
        
            elif choice_1 == 2:
                ask_sub = input("Enter the subject to be changed: ")
                ask_roll = input("Enter the student's roll: ")
                new_sub = input("Enter the new subject to be stored: ")
                self.classroom[ask_roll][ask_sub] = new_sub
                print(self.classroom)

            elif choice_1 == 3:
                ask_name = input('Enter whose marks to be updated: ')
                ask_roll = input("Enter that student's roll: ")
                self.classroom[ask_roll]['Mark'] = int(input('Enter new marks: '))
                print(self.classroom)

            else:
                print("PLease enter a valid choice.")
                exit()

        

obj = classroom()
n = int(input('Enter the number of students to be added: '))

for i in range(n):
    roll = int(input('Enter the roll number: '))
    name = input('Enter the name of th student: ')
    subject = input('Enter the subject name: ')
    mark = int(input('Enter the marks obtained in {}: '.format(subject)))

    obj.collectinfo(roll,name,subject,mark)