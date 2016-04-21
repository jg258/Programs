#__author__ = 'Jason'
# !/usr/bin/python
# Authors@ Jason Guo
# Date Made: 2/15/16
# Date Modified: 2/24/16
# ChangeLog/Function:
# Further Updated methods to lay groundwork to string comparison of vaccine string over genome string
# Implemented string alignment completely, added infrastructure to csvfile reader and plans for csvwriter
# Future feature to add more usability to interface, as well as multifile programming setup (object oriented)
# Bugs:
#   Count: 0

import math
import csv
import sys

class StatisticsComputation():
    def __init__ (self):
        self.totalCountMatch = 0
        self.xRangeConstant = 1.0/100.0
        self.yRangeConstant = 1.0/100.0
        self.history = 0
        self.filenamesVaccines = []
        self.filenamesGenomes = []
        self.countInRange = []
        self.xRange = []
        self.yRange = []

        self.main()

    def main(self):
        exitV = 0
        pathKingdoms = ""
        pathReference = ""

        while exitV != 1:
            print("************************************************************************")
            print("[1] Input Kingdom Reference CSV path")
            print("[2] Input Reference CSV path")
            print("[3] Execute Statistics Computation and Exit")
            print("************************************************************************")
            print("Please Choose A Number For Desired Operation")
            sys.stdout.flush()
            response = raw_input()

            if response == "1":
                print "Please input CSV Path for Kingdoms"
                pathKingdoms = raw_input()

                with open(pathKingdoms, "r") as acessedFile:
                    pass

            if response == "2":
                while exitV != 1:
                    print "Please input reference CSV (Setup: Protegen, Genome Sequence/Vaccine, Genome Complete"
                    pathReference = raw_input()
                    print "Is this correct?: " + pathReference
                    if raw_input().upper() == "Y":
                        exitV = 1

                print "Loading CSV..."
                self.importCSV(pathReference)
                exitV = 0

            if response == "3":
                for i in range(len(self.filenamesVaccines)):
                    genomeTemp = self.readTextFile(self.filenamesGenomes[i])
                    vaccineTemp = self.readTextFile(self.filenamesVaccines[i])

                    self.alignmentCheck_NoOverage(vaccineTemp, genomeTemp)

                exitV = 1


    def alignmentCheck_NoOverage(self, vaccineIn, genomeIn):
        countInRangeL = 0
        lengthVaccine = len(vaccineIn)
        lengthGenome = len(genomeIn)

        for i in range(lengthGenome/lengthVaccine):
            genomeTemp = genomeIn[i:i+lengthVaccine]
            for j in range(len(genomeTemp)):
                if genomeTemp[j:j+1] == vaccineIn[j:j+1]:
                    countInRangeL += 1

            self.countInRange.append(countInRangeL)
            self.xRange.append(self.xRangeConstant*i)
            self.yRange.append(self.yRangeConstant*i)


    def alignmentCheck_Overage(self, vaccineIn, genomeIn):
        xRange = []
        yRange = []
        countInRange = []
        lengthVaccine = len(vaccineIn)
        lengthGenome = len(genomeIn)

        for i in range(len(genomeIn)):
            for j in range(len(vaccineIn)):
               pass


    def readTextFile(self, filename):
        text = ""
        with open("C:\Users\Jason\Documents\Genomes\\" + filename + ".xml") as f:
            print "\nReading File..."

            startLineOffset = len( f.readline() )   #Reads first line (identifer line therefore not needed to be processed
            f.seek(startLineOffset)                 #Skips/starts file to be read where the genome starts

            for lines in f:
                lines = lines.replace("\n","")
                text += lines

        print "Finished!"
        return text


    def importCSV(self, csvName):
        with open(csvName, "rb") as csvFile:
            readIn = csv.reader(csvFile)
            readIn.next()
            for row in readIn:
                for i in range(len(row)-1):
                    if i == 0 and row[i+1].isdigit() == True and row[i+2].isdigit() == True:
                        self.filenamesVaccines.append(row[0]+"_"+row[i+1]+"_GS")

                    elif i == 1 and row[i].isdigit() == True and row[i+1].isdigit() == True:
                        self.filenamesGenomes.append(row[0]+"_"+row[i+1]+"_G")

                    elif i >= 2 and row[i].isdigit() == True and row[i+1].isdigit() == True:
                        self.filenamesGenomes.append(row[0]+"_"+row[i+1]+"_G")

            print "Finished Importing!"



x = StatisticsComputation()