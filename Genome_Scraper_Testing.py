# !/usr/bin/python
# Authors@ Courtney Astore and Jason Guo
# Date Made: Unknown/ Earlier in 2015?
# Date Modified: 2/23/16
# ChangeLog/Function:
# Updated to allow for future object oriented programming/integration into UI as well as parallel processing structure
#   added bug tracker log in comments
# Known Bugs:
#   Current number: 1
#   Issue #1: Program generating excess copies of NCBI ID's - Incorrect protogen ID with extra NCBI ID's

from Bio import Entrez
import os
import csv
import sys

class GenomeScraper_Testing():
    def __init__(self):
        self.sequenceFilenameList = []	    #format to be put in should be #_#########
        self.idNumberList = []	                #format should be ##########
        self.exitV = 0
        self.correctIn = 0
        self.history = 0

        self.main()


    def parseFiles(self, itemName, idNumber, email1):     #define main call for Entrez
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


    def displayLists(self):
        print "\n ID Numbers:"
        print self.idNumberList
        print"\nFile Names:"
        print self.sequenceFilenameList


    def removeLastEntry(self):
        del self.idNumberList[len(self.idNumberList)-1]
        del self.sequenceFilenameList[len(self.sequenceFilenameList)-1]
        self.displayLists()


    def importCSVFilenames(self):
        with open("Collecting_Seq_Genomes_IDs_INORDER.csv", "rb") as csvFile:
            readIn = csv.reader(csvFile)
            readIn.next()
            for row in readIn:
                if self.history > 0:
                    if int(row[0]) >= self.history:
                        for i in range(len(row)-1):
                            if i == 0 and row[i+1].isdigit() == True:
                                self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_GS")
                                self.idNumberList.append(row[i+1])

                            elif i == 1 and row[i+1].isdigit() == True:
                                self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_PS")
                                self.idNumberList.append(row[i+1])

                            elif i >= 2 and row[i+1].isdigit() == True:
                                self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_G")
                                self.idNumberList.append(row[i+1])
                else:
                    for i in range(len(row)-1):
                        if i == 0 and row[i+1].isdigit() == True:
                            self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_GS")
                            self.idNumberList.append(row[i+1])

                        elif i == 1 and row[i+1].isdigit() == True:
                            self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_PS")
                            self.idNumberList.append(row[i+1])

                        elif i >= 2 and row[i+1].isdigit() == True:
                            self.sequenceFilenameList.append(row[0]+"_"+row[i+1]+"_G")
                            self.idNumberList.append(row[i+1])
            print "Finished Importing!"


    def main(self):
        while self.exitV != 1:
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
                self.idNumberList.append(idNumberIN)

                print "Please Type File Name (##_########_GS/PS/G)"
                fileNameIN= raw_input()
                self.sequenceFilenameList.append(fileNameIN)

            elif response == "2":
                self.displayLists()

            elif response == "3":
                 if len(self.idNumberList) >0:
                     self.removeLastEntry()
                 else:
                     print "Nothing To Remove!"

            elif response == "4":
                self.importCSVFilenames()

            elif response == "5":
                self.exitV= 0
                while self.exitV ==0:
                    print "Please enter last outputted entry"
                    self.history = raw_input()
                    print "Is this correct?: " + self.history
                    if raw_input().upper() == "Y":
                        self.exitV = 1
                self.exitV = 0

            elif response == "6":
                while self.correctIn == 0:
                    print "Please enter email address"
                    email1 = raw_input()
                    print email1 + " is this correct? (Y/N)"
                    if raw_input().upper() == "Y":
                        self.correctIn = 1

                for i in range(len(self.idNumberList)):
                    self.parseFiles(self.sequenceFilenameList[i], self.idNumberList[i],email1)
                print "\nGoodbye!"
                self.exitV = 1

            else:
                print "\nERROR Unknown Input Choice!"

x = GenomeScraper_Testing()