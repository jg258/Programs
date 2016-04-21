__author__ = 'Jason'
#For Courtney To Help Her Along Her Way

import os

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

foundLimiter = 0    #Limiter to Escape Comparison Loop Once Match Is Found

def stringCheck(sequence):
    if len(sequence)%3 == 0:
        print "Length Is " + str(len(sequence)) + " Which Is Divisible By 3"
        return 1
    else:
        print "Length Is " + str(len(sequence)) + " Which Is Not Divisible By 3"
        return 0


def stringProcess(sequence):
    global foundLimiter
    i = 0
    limiter = 0
    dictionaryLoop = 0

    while i < len(sequence) and limiter != len(sequence)/3:
        print "\n" + sequence[i:i+3] + " DEBUG SUBSTRING"
        print str(i) + " DEBUG SUBSTRING RANGE"

        for key in proteinReference:            #Initial Loop to access array
            print key + " DEBUG KEY"
            print str(foundLimiter) + " FOUNDLIMITER DEBUG "
            print str(dictionaryLoop) + " DICTIONARYLOOP DEBUG"

            if foundLimiter == 0:
                for item in proteinReference[key]:          #Nested loop to get array items and compare to sequence
                    print item + " DEBUG ITEM ARRAY"

                    if foundLimiter == 0:
                        if sequence[i:i+3] == item:
                            print "Match Found! DEBUG"
                            sequenceBreakDown.append(key)
                            print sequenceBreakDown     #Debug to show end result
                            i += 3

                            foundLimiter = 1
                            dictionaryLoop += 1
                            break

                        elif sequence[i:i+3] != item and dictionaryLoop > 21:
                            print "No Match Found! DEBUG"

                            foundLimiter = 1
                            dictionaryLoop = 0
                            break

                        elif sequence[i:i+3] != item and dictionaryLoop < 21:
                            print "No Match Found...Still Searching DEBUG"
                            print dictionaryLoop

                        elif i >= len(sequence) and sequence[i:len(sequence)] == item:
                            print "Match Found! DEBUG"
                            sequenceBreakDown.append(key)
                            print sequenceBreakDown     #Debug to show end result
                            i += 3

                            foundLimiter = 1
                            dictionaryLoop += 1
                            break

                        else:
                            sequenceBreakDown.append("IDKY")
                            print sequenceBreakDown     #Debug to show end result

                            foundLimiter = 1
                            dictionaryLoop += 1
                    else:
                        break
            else:
                break

        dictionaryLoop += 1

        print "\n"
        print str(limiter) + " LIMITER DEBUG"

        if foundLimiter == 1:
            limiter += 1

            print sequenceBreakDown     #Debug to show end result
            foundLimiter = 0            #Resets Limit for Comparison Loop

        else:
            pass

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

if test == 1:
    stringProcess(text)




