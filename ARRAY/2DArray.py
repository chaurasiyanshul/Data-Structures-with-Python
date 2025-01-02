import numpy

twoDArray = numpy.array([[11,15,10,6],[10,14,11,50],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

# Insertion in 2d Array

new2D = numpy.insert(twoDArray, 0, [[1,2,3,4]], axis = 1)
print(new2D)


# Access the element in 2D Array 

def AccessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')

    else:
        print(array[rowIndex][colIndex])

print(AccessElements(new2D, 2,3 ))


def traverse2D(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

print(traverse2D(twoDArray))


def Search2D(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at Index ' + str(i)+" "+str(j)

    return "The element is not Found"


print(Search2D(new2D, 14))


# Deletion in 2d Array
Delete2D = numpy.delete(new2D ,0, axis = 1)
print(Delete2D)