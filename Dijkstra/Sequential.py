from time import clock
#Adjacency List
listA = [('A',0), ('H',8), ('B',4)]
listB = [('B',0), ('A',4), ('H',11), ('C',8)]
listC = [('C',0), ('B',8), ('I',2), ('F',4),('D',7)]
listD = [('D',0), ('C',7), ('F',5), ('E',9)]
listE = [('E',0), ('D',9), ('F',10)]
listF = [('F',0), ('C',4), ('D',14), ('E', 10)]
listG = [('G',0), ('H',1), ('I',6), ('F', 2)]
listH = [('H',0), ('A',8), ('B',11), ('I', 7), ('G', 1)]
listI = [('I',0), ('H',7), ('G',6), ('C', 2)]
bigList = []
visited = []
bigList.append(listA)
bigList.append(listB)
bigList.append(listE)
bigList.append(listD)
bigList.append(listC)
bigList.append(listF)
bigList.append(listG)
bigList.append(listH)
bigList.append(listI)
visitedNum = 0
size = len(bigList)
current = bigList[0]
#End vertex of the graph
endNode = 'H'
distance = 0
inside = False
ifInside = 0
tempDistance = 2147483647
smallestNode = ('MAX',2147483647)
finalDistance = 0

#Function to find the index of a list containing the given character
def findNode(lastlist):
    index = -1
    llindex = findIndex(lastlist)
    for i in range(1, len(bigList[llindex])):
                   if bigList[llindex][i][0]==lastlist:
                      index = i
    return index

#Function to find the index of a list given the parent node
def findIndex(node):
    index = -1
    for i in range(1, len(bigList)):
                   if bigList[i][0][0]==node:
                      index = i
    return index
start_time = clock()
#Main function that uses the Dijsktra Algorithm to find the sortest path
while endNode not in visited:
    if current[0][0] not in visited:
        for i in range(1, len(current)):
            if current[i][0] not in visited and current[i][1] \
                <= smallestNode[1] and current[i][1] + distance \
                <= tempDistance:
                tempDistance = current[i][1] + distance
                smallestNode = current[i]
            if current[i][0] == endNode:
                inside = True
                ifInside = current[i][1]
        visited += current[0][0]
        current = bigList[findIndex(smallestNode[0])]
        finalDistance = tempDistance
        distance = tempDistance
        tempDistance = 2147483647
        smallestNode = ('MAX', 2147483647)
        if inside:
            index = findIndex(visited[len(visited) - 1])
            if index == -1:
                visited += endNode
                finalDistance += ifInside
            if not bigList[index][findNode(endNode)][1] + distance \
                < distance + ifInside and len(bigList[index])>1:
                visited += endNode
                finalDistance += ifInside
                break
        print (current)
end_time = clock()
time = end_time-start_time
print('time is: ')
print(time)
print(visited)
    
