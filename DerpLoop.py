__author__ = 'Jason'
#For Courtney To Help Her Along Her Way

sequenceBreakDown = []
proteinBreakDown = []

proteinReference = {"TTT" :"Phenylalanine",  "TTA": "Leucine", "ATT":"Isoleucine", "ATG":"Methionine", "GTT": "Valine",
    "TCT" : "Serine", "CCT" : "Proline", "ACT":"Threonine"}


def stringCheck(sequence):
    if len(sequence)%3 == 0:
        print "Length Is " + str(len(sequence)) + " Which Is Divisible By 3"
        return 1
    else:
        print "Length Is " + str(len(sequence)) + " Which Is Not Divisible By 3"
        return 0

def stringProcess(sequence):
    i = 0
    limiter = 0
    while i < len(sequence) and limiter != len(sequence)/3:
        print sequence[i:i+3]
        print i

        if i >= len(sequence) and proteinReference.has_key(sequence[i:i+3]):
            sequenceBreakDown.append( proteinReference[sequence[i:len(sequence)]] )

        elif i < len(sequence) and proteinReference.has_key(sequence[i:i+3]):
            sequenceBreakDown.append( proteinReference[sequence[i:i+3]] )
            i += 3

        else:
            sequenceBreakDown.append("IDKY")
            i += 3

        limiter += 1

    print sequenceBreakDown


for i in range(10):
    print "\nPlease input Text"
    text = raw_input()
    test = stringCheck(text)

    if test == 1:
        stringProcess(text)

    print "Derp"