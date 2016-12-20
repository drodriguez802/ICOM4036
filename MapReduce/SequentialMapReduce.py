import time, re

words = {}
start = time.clock()
with open('ulyss12.txt') as inputfile:
    for line in inputfile:
        tokenizedLine = line.split()
        
        for token in tokenizedLine:
            token = re.sub(r"[^A-Za-z]+", '', token).lower()
            if token in words:
                words[token.lower()] += 1
        
            else:
                words[token.lower()] = 1


allWordSortDesc = sorted(words.items(), key=lambda x:x[1], reverse=True)
finish = time.clock()
total = finish-start
allWordSortDesc = allWordSortDesc[:100]
f = open("WordCount.txt", "w")
f.write("Execution time was: " + str(total)+"\n")
f.write("\n".join(map(lambda x: str(x), allWordSortDesc)))
f.close()
