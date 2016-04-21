__author__ = 'Jason'
#Version: 3.5
"""CHANGELOG:
    MAJOR:
        Fixed string processing to better read files
        Fixed string processing to more accurately pick up known sequences
        Fixed debug of unknown codon sequences
    Minor:
        Updated format of code for readability and addition of a changelog
"""
#For Courtney and her Project


class ProteinSequencer:
    def __init__(self):
        pass

    proteinReference = {'Lysine': ['AAA', 'AAG'], 'Aspartic_Acid': ['GAT', 'GAC'], 'Tryptophan': ['TGG'],
                        'Alanine': ['GCT', 'GCC', 'GCA', 'GCG'], 'Glycine': ['GGT', 'GGC', 'GGA', 'GGG'],
                        'Glutamine': ['CAA', 'CAG'], 'Arginine': ['AGA', 'AGG'], 'Phenylalanine': ['TTT', 'TTG'],
                        'Asparagine': ['AAT', 'AAC'], 'Glutamic_Acid': ['GAA', 'GAG'], 'Leucine': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
                        '~': ['TAA', 'TAG', 'TGA'], 'Methionine': ['ATG'], 'Histidine': ['CAT', 'CAC'],
                        'Valine': ['GTT', 'GTC', 'GTA', 'GTG'], 'Cysteine': ['TGT', 'TGC'],
                        'Isoleucine': ['ATT', 'ATC', 'ATA'], 'Threonine': ['ACT', 'ACC', 'ACA', 'ACG'],
                        'Proline': ['CCT', 'CCC', 'CCA', 'CCG'], 'Serine': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
                        'Tyrosine': ['TAT', 'TAC']}


    def sequenceDNAtoProtein(self, sequenceSegment):
        proteinBreakDown = []
        unknownProteins = []

        c = 0
        loopLimit = 0
        proteinFound = 0

        while( len(proteinBreakDown) < len(sequenceSegment)/3):     #Loops for processed length of sequenceSegment
            for proteinKey in self.proteinReference:
                print "DEBUG PROTEIN: " + proteinKey

                for sequence in self.proteinReference[proteinKey]:
                    print "DEBUG CODON: " + sequence
                    print "DEBUG TESTING: " + sequenceSegment[c:c+3]
                    print "DEBUG LIMITER: " + str(loopLimit)

                    if proteinFound == 0:

                        if sequence == sequenceSegment[c:c+3]:
                            proteinBreakDown.append(proteinKey)
                            proteinFound = 1
                            c += 3
                            print "DEBUG FOUND!: " + proteinKey

                        elif sequence != sequenceSegment[c:c+3] and loopLimit < 21:
                            print "DEBUG: Next Sequence"
                            #pass

                        else:
                            pass

                    else:
                        pass

                if proteinFound == 0:
                    loopLimit += 1

            if proteinFound == 0 and loopLimit >=21:  #Used to add unknown sequences as well as errors to pBreak
                print "DEBUG NO MATCHES"

                if unknownProteins.count(sequenceSegment[c:c+3]) == 0:
                    unknownProteins.append(sequenceSegment[c:c+3])

                proteinBreakDown.append("ERROR")
                c += 3

            loopLimit = 0
            proteinFound = 0

        print proteinBreakDown
        print "\n"
        print unknownProteins


    def processTextFileInput(self):
        text = ""
        with open("19_10313991.txt") as f:
            print "\nReading File..."

            startLineOffset = len( f.readline() )   #Reads first line (identifer line therefore not needed to be processed
            f.seek(startLineOffset)                 #Skips/starts file to be read where the genome starts

            for lines in f:
                if len(text)%3 == 0 and text != '':
                    self.sequenceDNAtoProtein(text)
                    text = ""

                else:
                    lines = lines.replace("\n","")
                    text += lines
                    print text

        print "Finished!"

x = ProteinSequencer()

x.processTextFileInput()
