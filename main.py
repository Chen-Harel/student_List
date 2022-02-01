students = []
def student_list():
    cont = "yes"
    while(cont =="yes"):
        method=input("What do you want to do? Type 'Load' to open and edit the list, 'View' to view the list, or 'Exit' to exit.").lower()
        if(method == "load"):
            f = open("student_file.txt", "a")
            
            student_dictionary={"name":"", "age":""}
            name = input("Enter a name:\n").capitalize()
            age = input("Enter age:\n")
            
            student_dictionary.update({"name":name})
            student_dictionary.update({"age":age})
            students.append(student_dictionary)
            
            save = input("Save and exit? Y or N.").capitalize()
            
            if save =="Y":
                f.write(str(students))
                f.close()
                print("List saved to file.")
                cont = "No"
        elif method == "view":
            viewFile()
        else:
            cont = "no"

def viewFile():
    f = open("student_file.txt", "r")
    students = f.read()
    print(students)
    f.close()

student_list()