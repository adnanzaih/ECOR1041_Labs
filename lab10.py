#lab 10
#Student: Adnan Hafeez 101210710

#Exercise 1
def count_evens(lst: list) -> int:
    """Returns the number of even integers in a list lst.
    >>> count_evens([-1,-2])
    1
    >>> count_evens([-1,-2,0,1,2,3,5,5,4,4])
    5
    >>> count_evens([])
    0
    """
    num_even = 0
    for item in lst:
        if item % 2 == 0:
            num_even += 1
        else:
            num_even += 0
    return num_even

#Exercise 2
def big_diff(lst: list) -> int:
    """Returns the difference between the maximum and minimum integer value in the given list lst. The input list must have at least 2 integers.
    >>> big_diff([10,3,5,6])
    7
    >>> big_diff([-10,3,5,6])
    16
    >>> big_diff([-5,-10,-1,-3])
    9
    """
    max_ = lst[0]
    min_ = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_:
            min_ = lst[i]
        if lst[i] > max_:
            max_ = lst[i]
    return max_ - min_

#Exercise 3
def has22(lst: list) -> bool:
    """Returns True if the list contains 2 next to a 2. Otherwise returns False.
    >>> has22([1,2,2,3])
    True
    >>> has22([4,2,3,2])
    False
    >>> has22([2])
    False
    >>> has22([])
    False
    """
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] and lst[i] == 2:
            return True
    return False

#Exercise 4
def centered_average(lst: list)-> float:
    """Returns the centered average of a list given at least 3 elements.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1,1,1])
    1.0
    >>> centered_average([-51,10,1,6,7,-51])
    -9.25
    """
    max_ = max(lst)
    min_ = min(lst)
    sum_ = 0
    for val in lst:
        sum_ += val
    return (sum_ - max_ - min_)/(len(lst)-2)

#Exercise 5
def sum13(lst: list)-> int:
    """Returns the sum of numbers in a list. Any value 13 and the immediate value after it is not counted.
    >>> sum13([1, 2, 2, 1, 13])
    6
    >>> sum13([13, 1, 2, 13, 2, 1, 13])
    3
    >>> sum13([13,-1,-5,5,13,-3])
    0
    """
    currentSum = 0
    if len(lst) == 0:
        return 0
    else:
        if lst[0] != 13:
            currentSum += lst[0]
        for i in range(len(lst)):
            if lst[i] != 13 and lst[i-1] != 13:
                currentSum += lst[i]
    return currentSum

# Exercise 6
def sum67(lst: list) -> int:
    """Returns the sum of a list, returning 0 for an empty list. The function will ignore sequences of integers
    encapsulated between 6 and 7 inclusive, starting with 6 and ending with 7.

    >>> sum67([1, 2, 2, 6, 99, 99, 7])
    5
    >>> sum67([-1,5,2,6,6,6,6,67,7,7,7,7])
    27
    >>> sum67([])
    0
    >>> sum67([1,2,6,100,7])
    3
    """
    ignore = False
    sum_ = 0
    for i in range(len(lst)):
        if ignore == False and lst[i] != 6:
            sum_ += lst[i]
        if ignore == False and lst[i] == 6:
            ignore = True
        if ignore == True and lst[i] == 7:
            ignore = False
    return sum_

#Exercise 7
def bank_statement(lst: list) -> list:
    """Returns a list of three numberrs: the first will be the sum of deposits,
    the second (a negative number) will be the sum of widthdrawals, and the third will be the account balance.
    >>> bank_statement([5000.00,-58.79,-110.00,-68.15,-2.52])
    [5000.0, -239.46, 4760.54]
    >>> bank_statement([1816.00,2500,480,-58.79,-110.00])
    [4796.0, -168.79, 4627.21]
    >>> bank_statement([1000,-1250])
    [1000, -1250, -250]
    """
    deposits_ = 0
    widthdrawals_ = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            widthdrawals_ += lst[i]
        else:
            deposits_ += lst[i]
    return [round(deposits_,2), round(widthdrawals_,2), round(deposits_ + widthdrawals_,2)]

#Exercise 8
def divisors(n: int)-> list:
    """
    Returns a list containing all the positive divisors of n.
    >>> divisors(6)
    [1, 2, 3, 6]
    >>> divisors(9)
    [1, 3, 9]
    >>> divisors(118)
    [1, 2, 59, 118]
    """
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst += [i]
    return lst

# Exercise 9
def reverse(lst: list) -> list:
    """Returns a new list that contains all the elements of the original list in reverse order.
    >>> reverse([1,2,3,4])
    [4, 3, 2, 1]
    >>> reverse([4,2,3,2])
    [2, 3, 2, 4]
    >>> reverse([])
    []
    """
    for i in range(len(lst) // 2):
        temp = lst[i]
        lst[i] = lst[-(i + 1)]
        lst[-(i + 1)] = temp
    return lst


# Automated Testing
def test_function(testing_functions: list, expected: list, test_cases: list) -> None:
    """
    Can be used to automatically test functions that return either a list, integer, bool or float.
    :param testing_functions: A list that contains all the function names to be tested.
    :param expected: A list that contains the expected results for each function being tested.
    :param test_cases: A list that contains all the test cases to be used as arguments for the functions being tested.
    """
    total_tests_passed = 0
    total_tests_done = 0
    for i in range(len(testing_functions)):
        _tests_passed = 0
        _tests = 0
        print("Testing function", testing_functions[i].__name__)
        print("**********************")
        for j in range(len(test_cases[i])):
            if expected[i][j] == float:
                if abs(testing_functions[i](test_cases[i][j]) - expected[i][j]) < 0.0001:
                    print("Checking whether " + testing_functions[i].__name__ + "(" + str(test_cases[i][j]) + ")", end="")
                    print(" = ", expected[i][j])
                    print("Test passed")
                    _tests_passed += 1
                    _tests += 1
                    total_tests_passed += 1
                    total_tests_done += 1
                else:
                    print("Checking whether " + testing_functions[i].__name__ + "(" + str(test_cases[i][j]) + ")", end="")
                    print(testing_functions[i](test_cases[i][j]))
                    print(" = ", expected[i][j])
                    print("Test failed")
                    _tests += 1
                    total_tests_done += 1
            else:
                if testing_functions[i](test_cases[i][j]) == expected[i][j]:
                    print("Checking whether " + testing_functions[i].__name__ + "(" + str(test_cases[i][j]) + ")",
                          end="")
                    print(" = ", expected[i][j])
                    print("Test passed")
                    _tests_passed += 1
                    _tests += 1
                    total_tests_passed += 1
                    total_tests_done += 1
                else:
                    print("Checking whether " + testing_functions[i].__name__ + "(" + str(test_cases[i][j]) + ")",
                          end="")
                    print(testing_functions[i](test_cases[i][j]))
                    print(" = ", expected[i][j])
                    print("Test failed")
                    _tests += 1
                    total_tests_done += 1
        print(_tests_passed,"tests passed for exercise",testing_functions[i].__name__)
        print(_tests-_tests_passed,"tests failed for exercise",testing_functions[i].__name__)
        print()
    print(total_tests_passed, "tests passed total")
    print(total_tests_done - total_tests_passed, "tests failed total")
    return None

test_function(
    testing_functions = [
        count_evens,
        big_diff,
        has22,
        centered_average,
        sum13,
        sum67,
        bank_statement,
        reverse,
        divisors],
    expected = [
        [1,5,0], #count_evens
        [7,16,9], #big_diff
        [True, False, False, False], #has22
        [5.2,1.0,-9.25], #centered_average
        [6,3,0], #sum13
        [5,27,0,3], #sum67
        [[5000.0, -239.46, 4760.54],[4796.0, -168.79, 4627.21],[1000, -1250, -250]], #bank_statement
        [[4, 3, 2, 1],[2, 3, 2, 4],[]], #reverse
        [[1, 2, 3, 6],[1, 3, 9],[1, 2, 59, 118]]], #divisors
    test_cases = [
        [[-1,-2],[-1,-2,0,1,2,3,5,5,4,4],[]], #count_evens
        [[10,3,5,6],[-10,3,5,6],[-5,-10,-1,-3]], #big_diff
        [[1,2,2,3],[4,2,3,2],[2],[]], #has22
        [[1, 1, 5, 5, 10, 8, 7],[1,1,1],[-51,10,1,6,7,-51]], #centered_average
        [[1, 2, 2, 1, 13],[13, 1, 2, 13, 2, 1, 13],[13,-1,-5,5,13,-3]], #sum13
        [[1, 2, 2, 6, 99, 99, 7],[-1,5,2,6,6,6,6,67,7,7,7,7],[],[1,2,6,100,7]], #sum67
        [[5000.00,-58.79,-110.00,-68.15,-2.52],[1816.00,2500,480,-58.79,-110.00],[1000,-1250]], #bank_statement
        [[1,2,3,4],[4,2,3,2],[]], #reverse
        [6,9,118] #divisors
    ])

#Do not put any code below this line
print("End of file reached successfully")
