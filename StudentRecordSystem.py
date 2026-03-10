student = {
   
}

studentName = input("Enter your name > ")
studentAge = int(input("Enter your age > "))
studentMarks = int(input("Enter your marks > "))

if len(studentName) <= 3 or len(studentName) > 15 : studentName = "Invalid name!"
if studentAge <= 0 or studentAge > 110 : studentAge = "Invalid age!"
if studentMarks <= 0 or studentMarks > 100 : studentMarks = "Invalid marks!"

student.update({
    "name" : studentName,
    "age" : studentAge,
    "marks" : studentMarks
})

wantView = input("Do you want to view your data (press 'y' for view or 'n' for skip) > ")

if wantView == "y" or wantView == "Y" : print(student)

wantUpdate = input("Do you want to update your data (press 'y' for view or 'n' for skip) > ")

if wantUpdate == "y" or wantUpdate == "Y" :
    studentName = input("Enter your name > ")
    studentAge = int(input("Enter your age > "))
    studentMarks = int(input("Enter your marks > "))
    student.update({
    "name" : studentName,
    "age" : studentAge,
    "marks" : studentMarks
}) 
    print("Here is your updated data : " , student)



wantdel = input("Do you want to delet your data (press 'y' for view or 'n' for skip) > ")

if wantdel == "y" or wantdel == "Y" :
    student.clear()
    print("Successfuly deleted!")
    print(student)
