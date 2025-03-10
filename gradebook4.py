import os

def printMenu():
    print("please select an option: ")
    print("1:build a new student")
    print("2:load a student from file")
    print("3:compute total grade")
    print("4:add grade to student")
    print("0:exit gradebook")
    choice = int(input("option: "))
    return choice

def buildAstudent():
    studentName = input("what is the students name: ")
    firstName, lastName = studentName.split(" ")
    fileName = firstName + "_" + lastName + ".txt"
    if (os.path.isfile(fileName)):
        print(f"error, {studentName} file already exists.")
    else:
        outputFile = open(fileName, "w")
        outputFile.write(studentName)
        outputFile.write("\n")
        addgrade = "YES"
        addgrade = input("add homework grade? (yes/no): ")
        while addgrade.upper() == "YES":
            print("grade input format: 98.5% without %")
            hwGrade = float(input("enter homework grade: "))
            outputFile.write(str(hwGrade))
            addgrade = input("add another grade? (yes/no): ")
            if addgrade.upper == "YES":
                outputFile.write(" ")
        outputFile.write("\n")
        #add lab grades
        addgrade = "YES"
        addgrade = input("add lab grade? (yes/no): ")
        while addgrade.upper() == "YES":
            print("grade input format: 98.5% without %")
            labGrade = float(input("enter lab grade: "))
            outputFile.write(str(labGrade))
            addgrade = input("add another grade? (yes/no): ")
            if addgrade.upper == "YES":
                outputFile.write(" ")
        outputFile.write("\n")
        #add test grades
        addgrade = "YES"
        addgrade = input("add test grade? (yes/no): ")
        while addgrade.upper() == "YES":
            print("grade input format: 98.5% without %")
            testGrade = float(input("enter test grade: "))
            outputFile.write(str(testGrade))
            addgrade = input("add another grade? (yes/no): ")
            if addgrade.upper == "YES":
                outputFile.write(" ")
        outputFile.write("\n")
        outputFile.close()
    
def loadAstudent():
    studentName = input("what is the students name: ")
    firstName, lastName = studentName.split(" ")
    fileName = firstName + "_" + lastName + ".txt"
    if (os.path.isfile(fileName)):
        inputFile = open(fileName, "r")
        hwgrades = []
        labgrades = []
        testgrades = []
        inputFile.readline()
        hwgrades = inputFile.readline().rstrip("\n").split(" ")
        labgrades = inputFile.readline().rstrip("\n").split(" ")
        testgrades = inputFile.readline().rstrip("\n").split(" ")
        print(f"homework grades: {hwgrades}")
        print(f"lab grades : {labgrades}")
        print(f"test grades : {testgrades}")
        return hwgrades, labgrades, testgrades, studentName
        inputFile.close()
    else:
        print(f"error, {studentname} file does not exist.")
        
def computegrade(hwgrades, labgrades, testgrades, studentName):
    print("weight input format: 98.5% without %")
    hwWeight = float(input("what is the hw weight: "))
    labWeight = float(input("what is lab weight: "))
    testWeight = float(input("what is test weight: "))
    
    hwtotal = 0.0
    for n in range(0, len(hwgrades)):
        hwtotal += float(n)
    hwAvg = hwtotal / len(hwgrades)
    
    labtotal = 0.0
    for n in range(0, len(labgrades)):
        labtotal += float(n)
    labAvg = labtotal / len(labgrades)
    
    testtotal = 0.0
    for n in range(0, len(testgrades)):
        testtotal += float(n)
    testAvg = testtotal / len(testgrades)
    
    courseAvg = (hwWeight * hwAvg) + (labWeight * labAvg) + (testWeight + testAvg)
    
    if courseAvg >= 90:
        lettergrade = 'A'
    elif courseAvg >= 80:
        lettergrade = 'B'
    elif courseAvg >= 70:
        lettergrade = 'C'
    elif courseAvg >= 60:
        lettergrade = 'D'
    else:
        lettergrade = 'F'
    #pls fix
    print(f"|{'student name':^20s}|{'course grade':^20s}|{'homework average':^20s}|{'labs average':^20s}|{'tests average':^20s}|")
    print(f"|{studentName:^20s}|{courseAvg:.2f} {lettergrade:^14s}|{hwAvg:.2f}|{labAvg:.2f}|{testAvg:.2f}|")
    
def addgrade(hwgrades, labgrades, testgrades, studentName):
    gameover = 'YES'
    while gameover.upper == 'YES':
        category = input("which category? (homework, labs, tests): ")
        if category.upper == 'HOMEWORK':
            grade = input("what is the homework grade?: ")
            inputFile = open(fileName, 'a')
            ##fix this
            #ask grade
            #add grade to list
            inputFile.close()
        gameover = input("would you like to add another grade? yes/no: ")
        #if so go back to start
    #if not compute final grade
    computegrade(hwgrades, labgrades, testgrades, studentName)
    
    #i have no idea what im doing 

def main():
    choice = printMenu()
    studentName = ""
    while choice != 0:
        if choice == 1:
            buildAstudent()
        elif choice == 2:
            hwgrades, labgrades, testgrades, studentName = loadAstudent()
        elif choice == 3:
            if studentName != "":
                computegrade(hwgrades, labgrades, testgrades, studentName)
            else:
                print("error, pls load student")
        elif choice == 4:
            if studentName != "":
                addgrade(hwgrades, labgrades, testgrades, studentName)
            else:
                print("error, pls load student")
        else:
            print("error, {choice} option not on list")
        choice = printMenu()
        
main()