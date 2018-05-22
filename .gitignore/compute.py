import collections


def initFile(file, size, aMax, records):  # insert records in dictionary
    line = None
    input = None
    firstLine = True
    for eachline in file:
        if (firstLine):
            aMax = eachline.rstrip()
            firstLine = False
        else:
            line = eachline.splitlines()
            input = line[0].split('|')
            name = records[input[0]]
            if (input[0] in records.keys()):
                name.append(input[1])
            else:
                name.append(' ')
            records[input[0]] = name

    for item in records.keys():
        if (len(records.get(item)) == size):
            name = records[item]
            name.append('')
            records[item] = name
    return aMax


def showStandardReport(list):
    col_width = max(len(str(word)) for row in list for word in row) + 2  # padding
    for row in list:
        print("".join(str(word).center(int(col_width)) for word in row))


def getAverage(component, studentDetails):
    data = []
    if (component == 1):
        for items in studentDetails:
            if (items.a1 == ''):
                data.append(0)
            else:
                data.append(int(items.a1))
    if (component == 2):
        for items in studentDetails:
            if (items.a2 == ''):
                data.append(0)
            else:
                data.append(int(items.a2))
    if (component == 3):
        for items in studentDetails:
            if (items.prj == ''):
                data.append(0)
            else:
                data.append(int(items.prj))
    if (component == 4):
        for items in studentDetails:
            if (items.t1 == ''):
                data.append(0)
            else:
                data.append(int(items.t1))
    if (component == 5):
        for items in studentDetails:
            if (items.t2 == ''):
                data.append(0)
            else:
                data.append(int(items.t2))
    return round(float(sum(data)) / float(len(studentDetails)), 2)


def generateStdReport(passPoint, records, a1Max, a2Max, pMax, t1Max, t2Max, sortingFactor):
    orderedRecords = records
    normalTable = []
    for items in orderedRecords:
        row = []
        id = items
        fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
        numeric_total = 0
        if (a1N != ''):
            numeric_total = numeric_total + float(a1N) / float(a1Max) * 7.5
        if (a2N != ''):
            numeric_total = numeric_total + float(a2N) / float(a2Max) * 7.5
        if (pr != ''):
            numeric_total = numeric_total + float(pr) / float(pMax) * 25
        if (t1N != ''):
            numeric_total = numeric_total + float(t1N) / float(t1Max) * 30
        if (t2N != ''):
            numeric_total = numeric_total + float(t2N) / float(t2Max) * 30

        grade = calcGrade(passPoint, numeric_total)
        row.append(id)
        row.append(ln)
        row.append(fn)
        row.append(a1N)
        row.append(a2N)
        row.append(pr)
        row.append(t1N)
        row.append(t2N)
        row.append(round(numeric_total,2))
        row.append(grade)
        normalTable.append(row)
        if (sortingFactor == 8):
            normalTable = sorted(normalTable, key=lambda x: x[sortingFactor], reverse=True)
        else:
            normalTable = sorted(normalTable, key=lambda x: x[sortingFactor])
    sortedTable = [['ID', 'LN', 'FN', 'A1', 'A2', 'PR', 'T1', 'T2', 'GR', 'FL']]
    for i in normalTable:
        sortedTable.append(i)
    showStandardReport(sortedTable)


def calcGrade(passPoint, grandTotal):
    grade = None
    interval = None
    interval = round(float(100 - passPoint) / 7.0, 2)
    if (grandTotal < passPoint):
        grade = 'F'
    else:
        if (grandTotal <= passPoint + interval):
            grade = 'C'
        else:
            if (grandTotal > passPoint + interval and grandTotal <= passPoint + 2 * interval):
                grade = 'B-'
            else:
                if (grandTotal > passPoint + 2 * interval and grandTotal <= passPoint + 3 * interval):
                    grade = 'B'
                else:
                    if (grandTotal > passPoint + 3 * interval and grandTotal <= passPoint + 4 * interval):
                        grade = 'B+'
                    else:
                        if (grandTotal > passPoint + 4 * interval and grandTotal <= passPoint + 5 * interval):
                            grade = 'A-'
                        else:
                            if (grandTotal > passPoint + 5 * interval and grandTotal <= passPoint + 6 * interval):
                                grade = 'A'
                            else:
                                if (grandTotal > passPoint + 6 * interval):
                                    grade = 'A+'
    return grade


def getData(component, records):
    componentTable = []
    orderedRecords = collections.OrderedDict(sorted(records.items()))
    if (component == 1):
        for items in orderedRecords:
            id = items
            row = []
            id = items
            fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
            fullName = ln + ', ' + fn  # Smith, Bob
            componentTable.append([id, fullName, str(a1N)])
    if (component == 2):
        for items in orderedRecords:
            id = items
            row = []
            id = items
            fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
            fullName = ln + ', ' + fn  # Smith, Bob
            componentTable.append([id, fullName, str(a2N)])
    if (component == 3):
        for items in orderedRecords:
            id = items
            row = []
            id = items
            fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
            fullName = ln + ', ' + fn  # Smith, Bob
            componentTable.append([id, fullName, str(pr)])
    if (component == 4):
        for items in orderedRecords:
            id = items
            row = []
            id = items
            fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
            fullName = ln + ', ' + fn  # Smith, Bob
            componentTable.append([id, fullName, str(t1N)])
    if (component == 5):
        for items in orderedRecords:
            id = items
            row = []
            id = items
            fn, ln, a1N, a2N, pr, t1N, t2N = orderedRecords.get(items)
            fullName = ln + ', ' + fn  # Smith, Bob
            componentTable.append([id, fullName, str(t2N)])
    return componentTable
