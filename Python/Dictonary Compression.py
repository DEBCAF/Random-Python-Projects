# Subroutines

def Enter():
    initial = ""
    while initial == "":
        initial = input("Enter your sentence: ")
    return initial 

def Discomp(initial):
    print("Original string:")
    print(initial)
    print()
    print("Size of original string (assuming 8-bit ASCII per char):", len(initial)*8, "bytes")
    print("---------------------------------------------------------------------------------------------")
    print()

def CreateLib(sentence):
    library = []
    count = 0
    index = 0
    words = sentence.split(" ")
    already = []
    print("Compressing...")
    for i in range(len(words)):
        if words[i] not in already:
            index = index + 1
            library.append([index, words[i]])
            already.append(words[i])
            count = count + 8*len(str(index))
            count = count + 8*len(words[i])
            print(index,":",words[i])
    print("Size of dictionary:",count,"bytes")
    return library

def SizeLib(library):
    count = 0
    for i in range(len(library)):
        count = count + 8*(len(str(library[i][0])))
        count = count + 8*(len(library[i][1]))
    return count 
        
def Comp(library, sentence, libsize):
    words = sentence.split(" ")
    complist = []
    count = 0
    for i in range (len(words)):
        for j in range (len(library)):
            if library[j][1] == words[i]:
                complist.append(str(library[j][0]))
                count = count + 8*len(str(library[j][0]))
    print("Contents of byte[] array replacing words with dict keys:",' '.join(complist))
    print("Size of byte[] array:", count, "bytes")
    print("Total compressed size = size of dictionary + size of byte[] array =", count+libsize, "bytes")
    print("This is", (count+libsize)/(8*(len(sentence)))*100, "percent of the original string")
    print("Compression rate = 100 -", (count+libsize)/(8*(len(sentence)))*100, "=", 100-(count+libsize)/(8*(len(sentence)))*100)
    print("---------------------------------------------------------------------------------------------")
    return complist

def Decomp(library, input):
    decomp = []
    print("Decompressing...")
    print("Decompressed string:")
    for i in range(len(input)):
        for j in range(len(library)):
            if int(library[j][0]) == int(input[i]):
                decomp.append(library[j][1])
    print(' '.join(decomp))
    
# Main program

sentence = Enter()
Discomp(sentence)
library = CreateLib(sentence)
comp = Comp(library, sentence, SizeLib(library))
Decomp(library, comp)