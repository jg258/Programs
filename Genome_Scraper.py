# !/usr/bin/python
# Authors@ Courtney Astore and Jason Guo
# Date Made: Unknown/ Earlier in 2015?
# Date Modified: 2/13/16
# ChangeLog/Function:
# Updated to allow importation of CSV files, planned update to allow for other delimited types of files, account access
# and greater history control for longer CSV files
#TEST PUSH COMMIT

from Bio import Entrez
import os
import csv
import sys


sequenceFilenameList = []	    #format to be put in should be #_#########
idNumberList = []	                #format should be ##########
exitV = 0
correctIn = 0
history = 0

def main(itemName, idNumber, email1):     #define main call for Entrez

    Entrez.email = email1
    filename = os.path.join('C:\Users\Jason\Documents\Genomes',str(itemName) + ".xml")



    if not os.path.isfile(filename):
        sys.stdout.write("Downloading: %s  \r" % itemName)

        net_handle = Entrez.efetch(db="nucleotide", id=idNumber, rettype="fasta", retmode="text")
        net_result = net_handle.read()
        net_handle.close()
        with open(filename, "w") as out_handle:
            out_handle.write(net_result)

        sys.stdout.write("Saved!")
        sys.stdout.flush()


def displayLists():
    print "\n ID Numbers:"
    print idNumberList
    print"\nFile Names:"
    print sequenceFilenameList


def removeLastEntry():
    del idNumberList[len(idNumberList)-1]
    del sequenceFilenameList[len(sequenceFilenameList)-1]
    self.displayLists()


while exitV != 1:
    print "\n\n\n***************************************************************"
    print "[1] Add Sequence/Item ID Number And Add Sequence/Item File Name"
    print "[2] Display Current List To Be Processed"
    print "[3] Remove Last Entry"
    print '[4] Import CSV File'
    print "[5] Enter last entry to start from"
    print "[6] Exit And Output"
    print "***************************************************************\n"

    print "Please Type Number For Desired Operation"

    response = raw_input()

    if response == "1":
        print "Please Type Sequence/Item ID Number (########)"
        idNumberIN = raw_input()
        idNumberList.append(idNumberIN)

        print "Please Type File Name (##_########_GS/PS/G)"
        fileNameIN= raw_input()
        sequenceFilenameList.append(fileNameIN)

    elif response == "2":
        displayLists()

    elif response == "3":
         if len(idNumberList) >0:
             removeLastEntry()
         else:
             print "Nothing To Remove!"

    elif response == "4":
        with open("Collecting_Seq_Genomes_IDs_INORDER.csv", "rb") as csvFile:
            readIn = csv.reader(csvFile)
            readIn.next()
            for row in readIn:
                if history > 0:
                    if int(row[0]) >= history:
                        for i in range(len(row)-1):
                            if i == 0 and row[i+1].isdigit() == True:
                                sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_GS")
                                idNumberList.append(row[i+1])
                            elif i == 1 and row[i+1].isdigit() == True:
                                sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_PS")
                                idNumberList.append(row[i+1])
                            elif i >= 2 and row[i+1].isdigit() == True:
                                sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_G")
                                idNumberList.append(row[i+1])
                else:
                    for i in range(len(row)-1):
                        if i == 0 and row[i+1].isdigit() == True:
                            sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_GS")
                            idNumberList.append(row[i+1])
                        elif i == 1 and row[i+1].isdigit() == True:
                            sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_PS")
                            idNumberList.append(row[i+1])
                        elif i >= 2 and row[i+1].isdigit() == True:
                            sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_G")
                            idNumberList.append(row[i+1])
        print "Finished Importing!"

    elif response == "5":
        exitV= 0
        while exitV ==0:
            print "Please enter last outputted entry"
            history = raw_input()
            print "Is this correct?: " + history
            if raw_input().upper() == "Y":
                exitV = 1
        exitV = 0

    elif response == "6":
        while correctIn == 0:
            print "Please enter email address"
            email1 = raw_input()
            print email1 + " is this correct? (Y/N)"
            if raw_input().upper() == "Y":
                correctIn = 1

        for i in range(len(idNumberList)):
            main(sequenceFilenameList[i], idNumberList[i],email1)
        print "\nGoodbye!"
        exitV = 1

    else:
        print "\nERROR Unknown Input Choice!"