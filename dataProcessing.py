import os
import csv

# create a new file to write to
writeTo = open('mergeFiles3.csv', 'a', newline='')
writeToCSV = csv.writer(writeTo)

# prompt for new directory
newDir = "C:\\Users\student\Desktop"


def combinecsv():

    for i in os.listdir(newDir):
        if i.endswith('.csv'):
            readFile = open(newDir + "\\" + i, 'r')
            readFileReader = csv.reader(readFile)

    next(readFileReader)

    for j in readFileReader:
        lastTwoColumns = [j[1], j[2]]
        writeToCSV.writerow(lastTwoColumns)

    readFile.close()

    writeTo.close()


def addData():
    tempFile = open("mergeFiles3.csv")
    tempFileReader = csv.reader(tempFile)

    writeTo = open('mergeFiles2.csv', 'a', newline='')
    writeToCSV = csv.writer(writeTo)


    for i in tempFileReader:
        tempFile2 = open('mergeFiles3.csv')
        tempFileReader2 = csv.reader(tempFile2)

        for j in tempFileReader2:
            if len(j) != 0:
                if i[0] == j[0]:
                    for k in tempFileReader2:
                        if i[0] == k[0]:
                            i[1] = int(i[1]) + int(k[1])

        i[1] = int(i[1])

        tempFile2.close()
        writeToCSV.writerow(i)


    tempFile.close()


def deleteDuplicates():
    f1 = csv.reader(open('mergeFiles2.csv', 'r'))
    writer = csv.writer(open('mergeFiles.csv', 'a', newline=''))
    product_numbers = set()

    writer.writerow(['Product', 'Total Quantity'])
    for row in f1:
        if row[0] not in product_numbers:
            writer.writerow(row)
            product_numbers.add(row[0])


combinecsv()
addData()
deleteDuplicates()
os.remove('mergeFiles3.csv')
os.remove('mergeFiles2.csv')