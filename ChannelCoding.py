import random

def channelCoding(cipherText):
    convolutionalCoding = dict()
    convolutionalCoding["00"] = {"0":("00","00"), "1":("10","11")}
    convolutionalCoding["01"] = {"0":("00","10"), "1":("10","01")}
    convolutionalCoding["10"] = {"0":("01","11"), "1":("11","00")}
    convolutionalCoding["11"] = {"0":("01","01"), "1":("11","10")}
    currentState = "00"

    channelEncodedText = list()

    for binary in cipherText:
        nextState,code = convolutionalCoding[currentState][binary]
        currentState = nextState
        channelEncodedText.append(code)

    return "".join(channelEncodedText)

def hammingDistance(code1,code2):
    if(len(code1) != len(code2)):
        print("Codes should be equal in size")
        return

    hammingDist = 0
    for i in range(0,len(code1)):
        hammingDist += abs(int(code1[i]) - int(code2[i]))
    return hammingDist

def findMinDistance(firstPathCost, secondPathCost):
    if(firstPathCost == secondPathCost):
        if(random.randint(0,1) == 0):
            return firstPathCost
        else:
            return secondPathCost
    if(firstPathCost > secondPathCost):
        return secondPathCost
    else:
        return firstPathCost

def findMinimumState(timeSlot):
    minimum = 2**32+1
    minimumState = "00"
    for state in timeSlot:
        if(timeSlot[state] < minimum):
            minimum = timeSlot[state]
            minimumState = state
    return minimumState


def channelDecoding(codeWord):
    Trellis = dict()
    Trellis["00"] = (["00","00","0"], ["01","10","0"])
    Trellis["01"] = (["10","11","0"], ["11","01","0"])
    Trellis["10"] = (["00","11","1"], ["01","01","1"])
    Trellis["11"] = (["10","00","1"], ["11","10","1"])
    states = ["00","01","10","11"]

    splitedCodeWord = list()
    for i in range(0,len(codeWord)):
        if(i%2 == 0):
            splitedCodeWord.append(codeWord[i] + codeWord[i+1])

    pathMetric = [dict() for i in range(0, len(splitedCodeWord)+1)]

    pathMetric[0]["00"] = 0
    pathMetric[0]["01"] = 2**32
    pathMetric[0]["10"] = 2**32
    pathMetric[0]["11"] = 2**32
    
    for i in range(0, len(splitedCodeWord)):
        for state in states:
            firstState,secondState = Trellis[state]

            firstPathCost = pathMetric[i][firstState[0]] + hammingDistance(splitedCodeWord[i], firstState[1])
            secondPathCost = pathMetric[i][secondState[0]] + hammingDistance(splitedCodeWord[i], secondState[1])

            bestPath = findMinDistance(firstPathCost, secondPathCost)
            pathMetric[i+1][state] = bestPath

    path = list()
    currentState = findMinimumState(pathMetric[len(pathMetric)-1])
    for i in range(len(splitedCodeWord)-1,-1,-1):
        firstState,secondState = Trellis[currentState]

        firstPathCost = pathMetric[i][firstState[0]] + hammingDistance(splitedCodeWord[i], firstState[1])
        secondPathCost = pathMetric[i][secondState[0]] + hammingDistance(splitedCodeWord[i], secondState[1])

        if(firstPathCost == secondPathCost):
            if(random.randint(0,1) == 0):
                currentState = firstState[0]
                path.append(firstState[2])
            else:
                currentState = secondState[0]
                path.append(secondState[2])
        elif(firstPathCost > secondPathCost):
            currentState = secondState[0]
            path.append(secondState[2])
        else:
            currentState = firstState[0]
            path.append(firstState[2])

    path.reverse()
    return "".join(path)