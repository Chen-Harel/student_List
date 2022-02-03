from importlib.resources import path
import os

students = []

def student_list():
    cont = "yes"
    while(cont =="yes"):
        method=input("What do you want to do? Type 'Create' to create a new file, 'Load' to open and edit the file, 'Remove' to delete a file, 'View' to view the file contents, or 'Exit' to exit.\n").lower()
        
        if(method == "load"):
            loadFile()
        elif method == "view":
            viewFile()
        elif method == "create":
            create()
        elif method == "remove":
            remFile()
        elif method == "exit":
            cont = "No"
        else:
            print("Please select a correct option...")

def viewFile():
    viewFiles()
    fileName = input("What file do you want to view? Type 'menu' to return to the main menu.\n")
    if os.path.exists(fileName+".txt"):
      f = open(fileName+".txt", "r")
      students = f.read()
      print(students)
      print("File is loaded...")
      f.close()
    elif fileName == "menu":
      student_list()
    else:
      print("File does not exist...")
      viewFile()

def create():
    fileName = input("Pick a name for your file...\n")
    f = open(fileName+".txt", "a")
    print("File has been created...")
    f.close()
    newFile = input("Create another file? Y or N.\n").lower()
    if newFile == "y":
        create()

def loadFile():
    cont = "yes"
    while (cont == "yes"):
        viewFiles()
        fileName = input("What file do you want do open?\n")
        f = open(fileName+".txt", "a")

        student_dictionary = {"name": "", "age": ""}
        name = input("Enter a name:\n").capitalize()
        age = input("Enter age:\n")

        student_dictionary.update({"name": name})
        student_dictionary.update({"age": age})
        students.append(student_dictionary)

        save = input("Save and exit? Y or N.\n").capitalize()

        if save == "Y":
            f.write(str(students))
            f.close()
            print("List saved to file.")
            cont = "No"
        elif save == "N":
            cont = "No"

def remFile():
    r = "yes"
    while r == "yes":
        viewFiles()
        remove = input("Select a file to delete or type 'menu' to go back to the main menu.\n")
        if os.path.exists(remove+".txt"):
            os.remove(remove+".txt")
            removeAgain = input("Delete another file? Y or N.\n").lower()
            if removeAgain == "y":
                remFile()
            elif removeAgain == "n":
                student_list()
            else:
                print("Select either Y or N.\n")
        elif remove == "menu":
            r = "no"
        else:
            print("File does not exist...")

def viewFiles():
  fileList = os.listdir()
  print(fileList)

student_list()
