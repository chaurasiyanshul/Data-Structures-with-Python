from array import *
# Create an array and traverse

my_arr = array('i', [1,2,3,4,5,6,7])

for i in my_arr:
    print(i)

# Access individual elements through indexes
print('step 2')
print(my_arr[4])

# Append any value in an array using insert() method
print('step 3')
my_arr.append(8)
print(my_arr)

# insert value in an array using insert() method
print('step 4')
my_arr.insert(6,11)
print(my_arr)

# Extend python array using extend() mehthod
print('step 5')
my_arr1 = array('i', [9,10,11,12])
my_arr.extend(my_arr1)
print(my_arr)

#  Add items from list into array using formlist()  method
print('step 6')
templist = [20,21,22]
my_arr.fromlist(templist)
print(my_arr)

# Remove any array element using remove() method
print('step 7')
my_arr.remove(11)
print(my_arr)
my_arr.remove(11)
print(my_arr)

# Remove last array element using pop() method
print('step 8')
my_arr.pop()
print(my_arr)

# Fetch any element through its index using index() method
print('step 9')
print(my_arr.index(21))

# Reverse a python array using reverse() method
print('step 10')
my_arr.reverse()
print(my_arr)

# Get array buffer information through buffer_info() method
print('step 11')
print(my_arr.buffer_info())

# check for number of occurences of an e(lement using count() method
print('step 12')
my_arr.append(20)
print(my_arr.count(20))
# convert array to string using tostring() method
print('step 13')
strTemp = my_arr.tobytes()
print(strTemp)
# convert array to a python list with same element using tolist() method
print('step 14')
print(my_arr.tolist())
# Append a string to char array using fromstring() method

# Slice elements from an array
print('step 14')
print(my_arr[1:4])





