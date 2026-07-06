
students = []

while True:

    print("\n===== Student Manager =====")

    print("1. Add Student")

    print("2. Remove Student")

    print("3. Show Students")

    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Student Name: ")

        students.append(name)

        print("Student Added!")

    elif choice == "2":

        name = input("Student Name to Remove: ")

        if name in students:

            students.remove(name)

            print("Student Removed!")

        else:

            print("Student Not Found!")

    elif choice == "3":

        print("\nStudent List:")

        for student in students:

            print("-", student)

    elif choice == "4":

        print("Good Bye!")

        break

    else:

        print("Invalid Choice!")
    
   
        
       
