matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

#to iteraste over all item

for row in matrix:
    for item in row:
        print(item)


# List methods/functions

number = [5,2,1,8,5,9]
number.insert(0,10)
number.remove(5)
number.append(25)
print(number)
number.pop()
print(number)
print(75 in number)
print(number.count(5))
number.sort()
print(number)
number.reverse()
print(number)

#progream to remove the duplicate in  a list

inputList=[2,5,6,3,8,9,4,6,7,3,5,4,7]
uniqueList=[]
for input in inputList:
    if input not in uniqueList:
        uniqueList.append(input)
print(uniqueList)



