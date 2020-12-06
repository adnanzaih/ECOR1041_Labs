#lab 9
#Student: Adnan Hafeez 101210710

#Exercise 1
def first_last6(lst: list) -> bool:
    """Returns True if lst's first, last or both element contain 6. Return's False otherwise.
    >>> first_last6([6,1,1,6])
    True
    >>> first_last6([6,1,1,0])
    True
    >>> first_last6([0,1,1,6])
    True
    >>> first_last6([6])
    True
    >>> first_last6([0,6,6,0])
    False
    """
    return lst[0] == 6 or lst[-1] == 6 or (lst[0] == 6 and lst[-1] == 6)

#Exercise 2
def same_first_last(lst: list) -> bool:
    """
    Returns True if lst is not empty and if the first and last elements are equal. lst must contain integers.
    >>> same_first_last([])
    False
    >>> same_first_last([1,2,2,1])
    True
    >>> same_first_last([-1,2,2,2,-1])
    True
    """
    if len(lst) > 0:
        return lst[0] == lst[-1]
    else:
        return False

#Exercise 3
def make_pi() -> list:
    """Returns the first three digits of pi.
    >>> make_pi()[0]
    3
    >>> make_pi()[1]
    1
    >>> make_pi()[2]
    4
    """
    return [3,1,4]

#Exercise 4
def common_end(lst: list, lst2: list) -> bool:
    """
    Returns True if the two input lists that are not empty have the same first element, or last element or if the first and last elements of both lists are the same.
    >>> common_end([],[])
    False
    >>> common_end([1,2,3],[1,5,4])
    True
    >>> common_end([1,2,3],[1,5,3])
    True
    >>> common_end([1,2,1],[2,5,2])
    False
    """
    if len(lst) > 0 and len(lst2) > 0:
        return lst[0] == lst2[0] or lst[-1] == lst2[-1] or (lst[0] == lst2[0] and lst2[-1] == lst2[-1])
    else:
        return False

#Exercise 5
def sum3(lst: list) -> int:
    """
    Returns the sum of all elements in lst. The lst must contain 3 integers.
    >>> sum3([1,2,3])
    6
    >>> sum3([1,1,1])
    3
    >>> sum3([-1,-2,-3])
    -6
    """
    return lst[0] + lst[1] + lst[2]

#Exercise 6
def rotate_left3(lst: list)-> list:
    """
    Returns a new list contain the elements of lst but rotated 1 step to the left. lst must contain 3 integer values.
    >>> rotate_left3([3,4,1])
    [4,1,3]
    >>> rotate_left3([1,2,3])
    [2,3,1]
    >>> rotate_left3([-1,2,-3])
    [2,-3,-1]
    """
    return [lst[1],lst[2],lst[0]]

#Exercise 7
def reverse3(lst: list)-> list:
    """Returns a new list containing the elements of lst in reverse order. lst must contain three integers.

    >>> reverse3([1,2,3])
    [3,2,1]
    >>> reverse3([-1,-2,3])
    [3,-2,-1]
    >>> reverse3([0,1,3])
    [3,1,0]
    """
    return [lst[2],lst[1],lst[0]]

#Exercise 8
def max_end3(lst: list) -> list:
    """
    Returns a list in which all the elements are initialized to the maximum value out of either the first or last element of lst. lst must contain three integers.
    >>> max_end3([2,9,20])
    [20,20,20]
    >>> max_end3([2,9,-20])
    [2,2,2]
    >>> max_end3([2,9,3])
    [3,3,3]
    """
    return [lst[0],lst[0],lst[0]] if lst[0] > lst[-1] else [lst[-1],lst[-1],lst[-1]]

#Exercise 9
def sum2(lst1: list) -> int:
    """
    Returns the sum of the first two elements of lst1. Returns 0 if lst is empty or if it only has one element.
    >>> sum2([1,2,3])
    3
    >>> sum2([])
    0
    >>> sum2([-1,-2,-3,-5])
    -3
    """
    if len(lst1) > 1:
        return lst1[0]+lst1[1]
    elif len(lst1) == 1:
        return len(lst1)
    else:
        return 0

#Exercise 10
def middle_way(lst1: list, lst2: list)->list:
    """
    Returns a list contain the middle value of lst1 and lst2. lst1 and lst2 must contain three integers.
    >>> middle_way([1,2,3],[4,5,6])
    [2,5]
    >>> middle_way([1,2,3],[1,1,1])
    [2,1]
    >>> middle_way([1,-1,3],[4,0,6])
    [-1,0]
    """
    return [lst1[1], lst2[1]]

#Exercise 11
def make_ends(lst: list)->list:
    """
    Returns a list made up of the first and last element in a given non empty list lst.
    >>> make_ends([4,5,6])
    [4,6]
    >>> make_ends([0])
    [0,0]
    >>> make_ends([1,2,3,4,-5])
    [1,-5]
    """
    return [lst[0], lst[-1]]

#Exercise 12
def has23(lst: list)-> bool:
    """
    Returns True if either or both elements in a 2 element list are equal to 2 or 3, otherwise returns False.
    >>> has23([1,6])
    False
    >>> has23([2,5])
    True
    >>> has23([2,3])
    True
    >>> has23([5,3])
    True
    """
    if lst[0] == 2 or lst[1] == 2:
        return True
    elif lst[0] == 3 or lst[1] == 3:
        return True
    else:
        return False



#Main Script
#Exercise 1 Tests
print("Exercise 1")
test1 = first_last6([6,1,1,6])
print(test1)
test2 = first_last6([6,1,1,0])
print(test2)
test3 = first_last6([0,1,1,6])
print(test3)
test4 = first_last6([6])
print(test4)
test5 = first_last6([0,6,6,0])
print(test5)

#Exercise 2 Tests
print("Exercise 2")
test1 = same_first_last([])
print(test1)
test2 = same_first_last([1,2,2,1])
print(test2)
test3 = same_first_last([-1,2,2,2,-1])
print(test3)

#Exercise 3 Tests
print("Exercise 3")
test1 = make_pi()[0]
print(test1)
test2 = make_pi()[1]
print(test2)
test3 = make_pi()[2]
print(test3)


#Exercise 4 Tests
print("Exercise 4")
test1 = common_end([],[])
print(test1)
test2 = common_end([1,2,3],[1,5,4])
print(test2)
test3 = common_end([1,2,3],[1,5,3])
print(test3)
test4 = common_end([1,2,1],[2,5,2])
print(test4)

#Exercise 5 Tests
print("Exercise 5")
test1 = sum3([1,2,3])
print(test1)
test2 = sum3([1,1,1])
print(test2)
test3 = sum3([-1,-2,-3])
print(test3)

#Exercise 6 Tests
print("Exercise 6")
test1 = rotate_left3([3,4,1])
print(test1)
test2 = rotate_left3([1,2,3])
print(test2)
test3 = rotate_left3([-1,2,-3])
print(test3)

#Exercise 7 Tests
print("Exercise 7")
test1 = reverse3([1,2,3])
print(test1)
test2 = reverse3([-1,-2,3])
print(test2)
test3 = reverse3([0,1,3])
print(test3)

#Exercise 8 Tests
print("Exercise 8")
test1 = max_end3([2,9,20])
print(test1)
test2 = max_end3([2,9,-20])
print(test2)
test3 = max_end3([2,9,3])
print(test3)

#Exercise 9 Tests
print("Exercise 9")
test1 = sum2([1,2,3])
print(test1)
test2 = sum2([])
print(test2)
test3 = sum2([-1,-2,-3,-5])
print(test3)

#Exercise 10 Tests
print("Exercise 10")
test1 = middle_way([1,2,3],[4,5,6])
print(test1)
test2 = middle_way([1,2,3],[1,1,1])
print(test2)
test3 = middle_way([1,-1,3],[4,0,6])
print(test3)

#Exercise 11 Tests
print("Exercise 11")
test1 = make_ends([4,5,6])
print(test1)
test2 = make_ends([0])
print(test2)
test3 = make_ends([1,2,3,4,-5])
print(test3)

#Exercise 12 Tests
print("Exercise 12")
test1 = has23([1,6])
print(test1)
test2 = has23([2,5])
print(test2)
test3 = has23([2,3])
print(test3)
test4 = has23([5,3])
print(test4)

#Do not put any code below this line
print("End of file reached successfully")
