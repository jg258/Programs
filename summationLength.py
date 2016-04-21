__author__ = 'Jason'

while exitV != 1:
                    print "Please input reference CSV (Setup: Protegen, Genome Sequence/Vaccine, Genome Complete"
                    pathReference = raw_input()
                    print "Is this correct?: " + pathReference
                    if raw_input().upper() == "Y":
                        exitV = 1

                print "Loading CSV..."
                self.importCSV(pathReference)
                exitV = 0

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