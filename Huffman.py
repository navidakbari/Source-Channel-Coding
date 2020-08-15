class Node:
    def __init__(self,prob,alphabet):
        self.prob = prob
        self.alphabet = alphabet
        self.left = None
        self.right = None

def generateNodes(alphabets, frequencies):
    Nodes = list()
    for i in range(0,len(alphabets)):
        Nodes.append(Node(float(frequencies[i]),alphabets[i]))

    return Nodes

def extractMin(Nodes):
    minIndex = 0
    minProb = Nodes[0].prob

    for i in range(0,len(Nodes)):
        if(Nodes[i].prob < minProb):
            minProb = Nodes[i].prob
            minIndex = i

    return minIndex


def inOrderIterator(root,dictionary,code):
    if(root.left == None and root.right == None):
        dictionary[root.alphabet] = code
        return
    inOrderIterator(root.left, dictionary, code+"1")
    inOrderIterator(root.right, dictionary, code+"0")

def generateHuffmanDictionary(alphabets, frequencies):
    Nodes = generateNodes(alphabets, frequencies)
    if(len(Nodes) == 0):
        return None
    if(len(Nodes) == 1):
        return {Nodes[0].alphabet:0}

    while(len(Nodes) != 1):
        left = Nodes[extractMin(Nodes)]
        Nodes.remove(left)
        right = Nodes[extractMin(Nodes)]
        Nodes.remove(right)

        parent = Node(left.prob + right.prob, left.alphabet + right.alphabet)
        parent.left = left
        parent.right = right
        Nodes.append(parent)

    root = Nodes[0]
    huffmanDictionary = dict()
    code = ""
    inOrderIterator(root,huffmanDictionary, code)
    return huffmanDictionary

def huffmanEncoding(codeBook, plainText):
    plainText = list(plainText)

    for i in range(0,len(plainText)):
        plainText[i] = codeBook[plainText[i]]

    return "".join(plainText)

def huffmanDecoding(huffmanDictionary, encodedData):

    decodedData = list()
    i = 0
    codeWord = ""

    while i < len(encodedData):
        codeWord += encodedData[i]
        if codeWord in huffmanDictionary.values():
            key_list = list(huffmanDictionary.keys()) 
            val_list = list(huffmanDictionary.values()) 
            decodedData.append(key_list[val_list.index(codeWord)])
            codeWord = ""
        i = i + 1

    return "".join(decodedData)