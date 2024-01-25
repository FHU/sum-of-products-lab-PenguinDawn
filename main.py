#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    finalList = []

    if len(list1) != len(list2):
        return "ERROR"
    for i in list1:
        for y in list2:
            newNum = int(i) * int(y)
            finalList.append(newNum)

    lastNum = 0
    for x in finalList:
        lastNum += x
    
    return lastNum 

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    pass