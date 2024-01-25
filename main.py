#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    finalList = []

    if len(list1) != len(list2):
        print("error")
    for i in range(0, len(list1)):
        newNum = int(list1[i]) * int(list2[i])
        print(newNum)
        finalList.append(newNum)
    lastNum = 0
    for x in finalList:
        lastNum += x
    
    print(lastNum) 

print(sum_of_products([1, 2, 3], [3, 2, 1]))
if __name__ == '__main__':
   input1 = int(input())
   input2 = int(input())
   sum_of_products(input1, input2)