import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)

# Insertion in Array Time C = o(n) Space c = o(1)


my_array1.insert(0, 6)
print(my_array1)

# Araay Traversal
arr = [1,2,3,4,5,6,7,8,9]

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr)



# import numpy

# np_array = numpy.array([], dtype = int)
# print(np_array)
# np_array1 = numpy.array([1,2,3,4,5])
# print(np_array1)