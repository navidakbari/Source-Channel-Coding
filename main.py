from Huffman import *
from noise import *
from ChannelCoding import *

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

fileStream = open("freq.txt","r")
frequencies = fileStream.read().split(",")

plainText = "navidakbari"

huffmanDictionary = generateHuffmanDictionary(alphabets, frequencies)

encodedText = huffmanEncoding(huffmanDictionary, plainText)
channelEncodedText = channelCoding(encodedText)
receivedText = noise(channelEncodedText)
channelDecodedText = channelDecoding(receivedText)
decodedText = huffmanDecoding(huffmanDictionary, channelDecodedText)

# print("Huffman Dictionary : ", huffmanDictionary)
print("Plain Text : ", plainText)
print("Encoded Text : ", encodedText)
print("Channel Encoded Text : ", channelEncodedText)
print("Received Text : ", receivedText)
print("Channel Decoded Text : ", channelDecodedText)
print("Decoded text : ",decodedText)