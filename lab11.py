#lab 11
#Student: Adnan Hafeez 101210710

#Exercise 1
#Step 1
point1 = [1.0,2.0]
point1

#What is displayed when Python evaluates point1?
#Python evalutes whats to the right of the equal sign, which is a list with two values. Two float objects are created 1.0,2.0
#respectively, and assigned to the list with index 0 and 1 respectively.
#finally Python then displays that list with its object values as [1.0,2.0]


#Step 2
point1.append(3.0)
point1
#What is displayed when Python evaluates point1?
#Answer [1.0,2.0,3.0]

point1.pop(0)
point1
#What is displayed when Python evaluates point1?
#[2.0,3.0]

point1.pop(0)
point1
#What is displayed when Python evaluates point1?
#[3.0]

#Step 3
point1 = (1.0,2.0)
type(point1)
point1
#What is displayed when Python evaluates point1?
#<class 'tuple'>
#(1.0,2.0)

#Step 4
x = point1[0]
y = point1[1]
#What is displayed when Python evaluates x and y?
#1.0
#2.0

point2 = (4.0,6.0)
x, y = point2
x
y
#What is displayed when Python evaluates x and y?
#4.0
#6.0

#Step 5
#What is displayed when Python evaluates this statement?
#Answer: TypeError: 'tuple' object does not support item assignment.
#>>> point2[0] = 2.0 # Can we change the point to (2.0, 6.0)?
#We cannot change the point to (2.0,6.0).

#What is displayed when Python evaluates this statement?
#Answer: AttributeError: 'tuple' object has no attribute 'append'
#>>> point2.append(4.0) # Can we add a third coordinate?
#We cannot add a third coordinate.


#What is displayed when Python evaluates this statement?
#Answer: AttributeError: 'tuple' object has no attribute 'pop'
#>>> point2.pop(0) # Can we remove the first coordinate?
#We cannot remove the first coordinate.

#Step 6
points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
points[0]
#Displays: (1.0,5.0)
points[1]
#Displays: (2.0,8.0)
points[2]
#Displays: (3.5,12.5)

# Exercise 2
def average(lst: list) -> list:
    """Returns a list of tuples with values equal to the integer average of the numbers in the tuple at the same position in lst.
    Pre-conditions: Each tuple inside the list lst must contain three non-negative integers.

    >>> average([(27,219,134),(1,2,3)])
    [(126, 126, 126), (2, 2, 2)]

    >>> average([(27,219,134)])
    [(126, 126, 126)]

    >>> average([(0,219,134)])
    [(117, 117, 117)]

    >>> average([])
    []
    """
    average_ = 0
    return_list = []
    for item in lst:
        x, y, z = item
        average_ = (x + y + z) // 3  # integer division
        return_tuple = (average_, average_, average_)
        return_list += [return_tuple]
    return return_list

#Exercise 3
points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
points
#What is displayed when points is evaluated?
#Answer: {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}


point1 = (1.0, 2.0)
point2 = (4.0, 6.0)
point3 = (10.0, -2.0)
points = {point1, point2, point3}
points
#What is displayed when points is evaluated?
#Answer: {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}

points = set()
points.add(point1)
points.add(point2)
points.add(point3)
points
#What is displayed when points is evaluated?
#Answer: {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}

#Step 2
points.add(point2)
points
#What happens if we try to insert a point that is already in the set?
#Answer: Nothing happens, sets can only contain distinct values, the extra addition is not added to the set,
#and the original set is displayed with no change.

#How many copies of the point (4.0,6.0) are in the set?
#Answer: exactly one copy.

#Can individual points in the set be retrieved by specifying an index (position)?
#Answer: sets are not index or ordered, individual values from a set using indexices cannot be retrived. Evaluating
#points[0] gives a TypeError: 'set' object is not subscriptable.

#Step 4

#What is displayed when the loop is executed?

for point in points:
    print(point)

#Answer: each tuple is printed on a seperate line as follows:
#(1.0, 2.0)
#(10.0, -2.0)
#(4.0, 6.0)


#Exercise 4
def sum_x(st: set)-> float:
    """Returns the sum of all x-coordinates given a set containing n points represented by a tuple containing two float values.
    The first float is coordinate x, and the second float is coordinate y.
    >>> sum_x({(1.0,3.0),(1.5,4.0),(5.9,1.0)})
    8.4
    >>> sum_x({(1.0,3.0)})
    1.0
    >>> sum_x({})
    0
    >>> sum_x({()})
    0
    """
    sum_x = 0
    for set_ in st:
        if len(set_) > 0:
            sum_x += set_[0]
    return sum_x

#Main Script
#Manual testing for exercise 2 and 4


#Exercise 2
print("Exercise 2")
testcase1 = average([(27,219,134),(1,2,3)]) #[(126, 126, 126), (2, 2, 2)]
print(testcase1)
testcase2 = average([(27,219,134)]) #[(126, 126, 126)]
print(testcase2)
testcase3 = average([(0,219,134)]) #[(117, 117, 117)]
print(testcase3)
testcase4 = average([])# []
print(testcase4)


#Exercise 4
print("Exercise 4")
testcase1 = sum_x({(1.0,3.0),(1.5,4.0),(5.9,1.0)}) #8.4
print(testcase1)
testcase2 = sum_x({(1.0,3.0)}) #1.0
print(testcase2)
testcase3 = sum_x({}) #0
print(testcase3)
testcase4 = sum_x({()})#0
print(testcase4)


#Do not put any code below this line
print("End of file reached successfully")
