
students={}

while True:
  print("_"*30)
  print("\n----Student Record Menu----")
  print("1. Add Student")
  print("2. Search Student by Roll No")
  print("3. Display All Students")
  print("4. Exit")
  print("_"*30)

  choice=input("Enter your choice  (1-4):")
  print("_"*30)

  if choice=="1":
    # add student to record
    roll=input("Enter Roll No: ")
    if roll in students:
      print("Student with this roll number already exists.")
      print("_"*30)
    else:
      name=input("Enter name:")
      marks=input("Enter marks:")
      contact=input("Enter contact number:")
      students[roll]={"name":name,"marks":marks,"contact":contact}
      print("Students added successfully")
      print("_"*30)

  elif choice=="2":
    #search the student by roll number
    roll=input("Enter Roll Number to search: ")
    if roll in students:
      student=students[roll]
      print(f"Name: {student['name']}")
      print(f"Marks: {student['marks']}")
      print(f"Contact: {student['contact']}")
      print("_"*30)
    else:
      print("Student not found. ")
      print("_"*30)

  elif choice=="3":   
    # Display the students records
    if not students:
      print("No Students found. ")
      print("_"*30)
    else:
      print("\n----All Student Details----")
      for roll,info in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Contact: {info['contact']}")
        print("_"*30)
  elif choice=="4":
    print("Thank you, Have a good day") 
    print("_"*30)
    break
  else:
    print("Invalid choice ")
    print("_"*30)




