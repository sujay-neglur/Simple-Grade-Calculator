from compute import initFile, generateStdReport, getAverage, getData, showStandardReport, calcGrade

# init student objects
class Students:
    def __init__(self, id, fName, lName, a1Marks, a2Marks, pMarks, t1Marks, t2Marks):
        self.id = id
        self.fname = fName
        self.lname = lName
        self.a1 = a1Marks
        self.a2 = a2Marks
        self.prj = pMarks
        self.t1 = t1Marks
        self.t2 = t2Marks

    def details(self):
        print("Id " + str(self.id))
        print("First name " + str(self.fname))
        print("Last name " + str(self.lname))
        print("a1 Marks " + str(self.a1))
        print("a2 Marks " + str(self.a2))
        print("prj Marks " + str(self.prj))
        print("t1 Marks " + str(self.t1))
        print("t2 Marks " + str(self.t2))


# put data in hash table
records = []
classes = open('class.txt', 'r+')
a1 = open('a1.txt', 'r+')
a2 = open('a2.txt', 'r+')
prj = open('project.txt', 'r+')
t1 = open('test1.txt', 'r+')
t2 = open('test2.txt', 'r+')
records = {}
studentDetails = []
for eachline in classes:
    line = eachline.splitlines()
    inputLine = line[0].split('|')
    records[inputLine[0]] = [inputLine[1], inputLine[2]]

a1Max = initFile(a1, 2, 0, records)
a2Max = initFile(a2, 3, 0, records)
pMax = initFile(prj, 4, 0, records)
t1Max = initFile(t1, 5, 0, records)
t2Max = initFile(t2, 6, 0, records)
# end put data in hash table


# create student objects
for items in records.keys():
    id = items
    details = records.get(items)
    fname, lname, a1Marks, a2Marks, pMarks, t1Marks, t2Marks = details
    studentDetails.append(Students(id, fname, lname, a1Marks, a2Marks, pMarks, t1Marks, t2Marks))

# end object creation
# function to display in the format

# take inputs

choice = None

while choice != 6:
    print('Enter choice')
    print('1. Display individual component')
    print('2. Display component average')
    print('3. Display Standard Report')
    print('4. Sort by alternate column')
    print('5. Change Pass/Fail point')
    print('6. Exit')
    choice = input()
    choice = int(choice)
    if (choice == 1):
        print("Select component:")
        print('1. A1')
        print('2. A2')
        print('3. PRJ')
        print('4. T1')
        print('5. T2')
        component = input()
        component = int(component)
        if (component == 1):
            a1Table = getData(1, records)
            print('A1 grades (' + str(a1Max) + ')')
            showStandardReport(a1Table)
        if (component == 2):
            a1Table = getData(2, records)
            print('A2 grades (' + str(a2Max) + ')')
            showStandardReport(a1Table)
        if (component == 3):
            a1Table = getData(3, records)
            print('PR grades (' + str(pMax) + ')')
            showStandardReport(a1Table)
        if (component == 4):
            a1Table = getData(4, records)
            print('T1 grades (' + str(t1Max) + ')')
            showStandardReport(a1Table)
        if (component == 5):
            a1Table = getData(5, records)
            print('T2 grades (' + str(t2Max) + ')')
            showStandardReport(a1Table)
    if (choice == 2):
        print("Select component:")
        print('1. A1')
        print('2. A2')
        print('3. PRJ')
        print('4. T1')
        print('5. T2')
        component = input()
        component = int(component)
        if (component == 1):
            a1Avg = getAverage(1, studentDetails)
            print('A1 average: ' + str(a1Avg) + '/' + str(a1Max))
        if (component == 2):
            a1Avg = getAverage(2, studentDetails)
            print('A2 average: ' + str(a1Avg) + '/' + str(a2Max))
        if (component == 3):
            a1Avg = getAverage(3, studentDetails)
            print('Prj average: ' + str(a1Avg) + '/' + str(pMax))
        if (component == 4):
            a1Avg = getAverage(4, studentDetails)
            print('T1 average: ' + str(a1Avg) + '/' + str(t1Max))
        if (component == 5):
            a1Avg = getAverage(5, studentDetails)
            print('T2 average: ' + str(a1Avg) + '/' + str(t2Max))

    if (choice == 3):
        stdReport=generateStdReport(50, records, a1Max, a2Max, pMax, t1Max, t2Max,0)

    if (choice == 4):
        print('Select alternate column')
        print('1. Last Name')
        print('2. GR')
        component = input()
        component = int(component)
        if (component == 1):
            generateStdReport(50,records,a1Max,a2Max,pMax,t1Max,t2Max,1)

        if (component == 2):
            generateStdReport(50, records, a1Max, a2Max, pMax, t1Max, t2Max, 8)
    if (choice == 5):
        print('Enter new passing point')
        point = input()
        point = float(point)
        generateStdReport(point,records,a1Max,a2Max,pMax,t1Max,t2Max,0)
    if (choice == 6):
        print('GoodBye')

