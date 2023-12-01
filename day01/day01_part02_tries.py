
## [FAIL]Exo 2
#result = 0
#with open(file_name, 'r') as input_file:
#    for line in input_file:
#        letterRep = line
#        for num in corresp:
#            print(num)
#            letterRep = letterRep.replace(num, corresp[num])
#            print(letterRep)

#        lineResult = re.findall('\d', letterRep)
#        calib = lineResult[0] + lineResult[-1]
#        result += int(calib)
#        print(calib)
#        #print(lineResult[0]
#print(result)

#def replace_num_letter(letterRep):
#    numIndexTable = {}

#    for num in corresp:
#        numIndex = letterRep.index(num) if num in line else 10000
#        if numIndex < 10000:
#            numIndexTable[num] = numIndex
#    #valueToReplaceFirst = numIndexTable[sorted(numIndexTable)[0]]
#    #valueToReplaceFirst = numIndexTable[sorted(numIndexTable.items(), key=lambda item: item[1])[0]]
#    valueToReplaceFirst = sorted(numIndexTable.items(), key=lambda item: item[1])[0][0]
#    lineRep = letterRep.replace(valueToReplaceFirst, corresp[valueToReplaceFirst])

#    if len(numIndexTable) != 0:
#        toto = replace_num_letter(lineRep)
#    else:
#        return toto

### Exo 2
#result = 0

#with open(file_name, 'r') as input_file:
#    for line in input_file:
#        letterRep = line
#        #for num in corresp:
#        #lineRep = replace_num_letter(lineRep)
#        letterRep = replace_num_letter(letterRep)
#        print(letterRep)

#        lineResult = re.findall('\d', letterRep)
#        calib = lineResult[0] + lineResult[-1]
#        result += int(calib)
#        print(calib)
#        #print(lineResult[0]
#print(result)
