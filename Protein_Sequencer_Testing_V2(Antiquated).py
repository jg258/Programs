__author__ = 'Jason'
#For Courtney and her Project

sequenceBreakDown = []
proteinBreakDown = []

proteinReference = {'Lysine': ['AAA', 'AAG'], 'Aspartic_Acid': ['GAT', 'GAC'], 'Tryptophan': ['TGG'],
                    'Alanine': ['GCT', 'GCC', 'GCA', 'GCG'], 'Glycine': ['GGT', 'GGC', 'GGA', 'GGG'],
                    'Glutamine': ['CAA', 'CAG'], 'Arginine': ['AGA', 'AGG'], 'Phenylalanine': ['TTT', 'TTG'],
                    'Asparagine': ['AAT', 'AAC'], 'Glutamic_Acid': ['GAA', 'GAG'], 'Leucine': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
                    '~': ['TAA', 'TAG', 'TGA'], 'Methionine': ['ATG'], 'Histidine': ['CAT', 'CAC'],
                    'Valine': ['GTT', 'GTC', 'GTA', 'GTG'], 'Cysteine': ['TGT', 'TGC'],
                    'Isoleucine': ['ATT', 'ATC', 'ATA'], 'Threonine': ['ACT', 'ACC', 'ACA', 'ACG'],
                    'Proline': ['CCT', 'CCC', 'CCA', 'CCG'], 'Serine': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
                    'Tyrosine': ['TAT', 'TAC']}


def stringCheck(sequence):
    if len(sequence)%3 == 0:
        print "Length Is " + str(len(sequence)) + " Which Is Divisible By 3"
        return 1
    else:
        print "Length Is " + str(len(sequence)) + " Which Is Not Divisible By 3"
        return 0

def sequenceDNAtoProtein(sequenceSegment):
    i = 0
    proteinFound = 0
    loopLimit = 0
    error = 0

    while(i < len(sequenceSegment)-3):
        for protein in proteinReference:

            if proteinFound == 0:            #IF TRUE= no match found, FALSE= match found
                print "DEBUG: PROTEIN KEY " + protein
                print "DEBUG: PROTEIN SEQUENCE BEING PROCESSED " + sequenceSegment[i:i+3]
                print "DEBUG: i Count " + str(i)

                for proteinSequence in proteinReference[protein]:
                    print "DEBUG: LOOPLIMITVAL: " + str(loopLimit)
                    print "DEBUG: PROTEINVAL: " + str(proteinFound)
                    print "DEBUG: ERRORVAL: " + str(error)
                    if proteinFound == 0:
                        print "DEBUG: COMPARING PROTEIN SEQUENCE " + proteinSequence + " TO " + sequenceSegment[i:i+3]

                        if sequenceSegment[i:i+3] == proteinSequence:  #IF TRUE= match found, FALSE= no match found
                            print "DEBUG: PROTEIN MATCH FOUND"

                            proteinBreakDown.append(protein)    #Adds found protein to protein breakdown list
                            proteinFound = 1

                        elif sequenceSegment[i:i+3] != proteinSequence and i <= len(sequenceSegment) and loopLimit < 60:   #IF TRUE= no match found but other proteins still needed to be compared
                            print "DEBUG: NO PROTEIN MATCH FOUND"


                        elif sequenceSegment[i:i+3] == proteinSequence and i <= len(sequenceSegment) and loopLimit < 60:   #IF TRUE= no match found but other proteins still needed to be compared
                            print "DEBUG: PROTEIN MATCH FOUND"

                            proteinBreakDown.append(protein)    #Adds found protein to protein breakdown list
                            proteinFound = 1


                        else:
                            print "DEBUG: UNKNOWN SCENARIO REVIEW DEBUG LOGS"
                            proteinBreakDown.append("ERROR")
                            proteinFound = 1
                            error = 1

                    else:
                        print "DEBUG: NESTED LOOP EXIT, MATCH FOUND"
                        break

                    loopLimit += 1


            elif proteinFound == 1 and i < (len(sequenceSegment)-3) and error == 0:
                print "DEBUG: MOVING TO NEXT SEGMENT TO BE PROCESSED"
                i += 3
                proteinFound = 0
                loopLimit = 0
                error = 0

            elif proteinFound == 1 and i < (len(sequenceSegment)-3) and error == 1:
                print "DEBUG: UNKNOWN ERROR DETECTED MOVING TO NEXT SEGMENT TO BE PROCESSED"
                i += 3
                proteinFound = 0
                loopLimit = 0
                error = 0

            else:
                print "DEBUG: LOOP EXIT"
                break

    print "\nFinished Processing!\n"
    print proteinBreakDown
    print str(len(proteinBreakDown))

#Actual Program Loop
print "\nReading File..."

with open("3_82698932.txt") as f:
    startLineOffset = len( f.readline() )
    print startLineOffset
    f.seek(startLineOffset)
    text = f.read(210)
    print text
    text = text.replace("\n","")

test = stringCheck(text)
print text
print len(text)


if test == 1:
    sequenceDNAtoProtein(text)


