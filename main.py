
def sum_of_products(list1, list2):
    finalList = []

    if len(list1) != len(list2):
        print("error")
    else:
    
        for i in range(0, len(list1)):
            newNum = int(list1[i]) * int(list2[i])
            finalList.append(newNum)

        lastNum = 0
        for x in finalList:
            lastNum += x
        print(lastNum)

#here it is
if __name__ == '__main__':
   input1 = input()
   input2 = input()
   #input1 = input1[0:-1]
   #input2 = input2[0:-1]
   list1 = input1.split(" ")
   list2 = input2.split(" ")
   sum_of_products(list1, list2)