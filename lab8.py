#Lab 8
#Student: Adnan Hafeez 101210710

#Exercise 1
def bakers_party(num_pastries: int, weekend: bool) -> bool:
    """
    Returns True of the bakers party is a success, and False if it's not. A baker's party is considered successful
    if its a weekend and the number of pastries is above or equal to 40. If a weekday, its considered a success only if the
    number of pastries is between 40 and 60 inclusive. num_pastries is the number of pastries at the party,
    and weekend if true means its saturday or sunday, otherwise its a weekday.

    >>> bakers_party(39, True)
    False
    >>> bakers_party(39, False)
    False
    >>> bakers_party(50, True)
    True
    >>> bakers_party(40, True)
    True
    >>> bakers_party(40, False)
    True
    >>> bakers_party(60, False)
    True
    >>> bakers_party(50, False)
    True
    >>> bakers_party(100, True)
    True
    >>> bakers_party(100, False)
    False
    """
    LOWER_LIMIT = 40
    UPPER_LIMIT = 60
    # if weekend==True:
    #     return num_pastries >=LOWER_LIMIT
    # else:
    #     return LOWER_LIMIT <= num_pastries <=UPPER_LIMIT
    return num_pastries >= LOWER_LIMIT if weekend else LOWER_LIMIT <= num_pastries <=UPPER_LIMIT


# Exercise 2
def squirrel_play(temp: int, summer: bool) -> bool:
    """
    Returns True if squirrels are playing, and False when they are not.
    Squirrels play between temperatures 60 to 90F when its not summer, and between 60 to 100F if its summer.
    Temperature is the temperature in F of the given day, and if summer is true, then the season is summer, otherwise
    its not.

    >>> squirrel_play(100, False)
    False
    >>> squirrel_play(100, True)
    True
    >>> squirrel_play(60, True)
    True
    >>> squirrel_play(70, False)
    True
    >>> squirrel_play(70, True)
    True
    >>> squirrel_play(60, False)
    True
    >>> squirrel_play(59, False)
    False
    """
    LOWER_TEMP = 60
    SUM_UPPER_TEMP = 100
    UPPER_TEMP = 90
    return LOWER_TEMP <= temp <= SUM_UPPER_TEMP if summer else LOWER_TEMP <= temp <= UPPER_TEMP


#Exercise 3
def great_42(a: int, b: int) -> bool:
    """Returns True if a or b are equal to 42, or if their sum or difference is equal to 42. Returns False otherwise.
    >>> great_42(-43, 85)
    True
    >>> great_42(-43,-85)
    True
    >>> great_42(43,-85)
    False
    >>> great_42(42,0)
    True
    >>> great_42(-42,0)
    True
    >>> great_42(-100,12)
    False
    """
    GREAT_NUM = 42
    return (a == GREAT_NUM or b == GREAT_NUM) or (a+b) == GREAT_NUM or abs(a-b) == GREAT_NUM

#Exercise 4
def blackjack(a: int, b: int) -> int:
    """
    Returns whichever value is closest to 21 without being over 21. Returns 0 if both values are over 21.
    a and b must be positive.
    >>> blackjack(19,20)
    20
    >>> blackjack(19,21)
    21
    >>> blackjack(17,22)
    17
    >>> blackjack(23,25)
    0
    >>> blackjack(14,17)
    17
    """
    LUCKY_NUM = 21
    if a <= LUCKY_NUM and b > LUCKY_NUM:
        return a
    elif b <= LUCKY_NUM and a > LUCKY_NUM:
        return b
    elif a > LUCKY_NUM and b > LUCKY_NUM:
        return 0
    else:
        if abs((LUCKY_NUM-a)) < abs((LUCKY_NUM-b)):
            return a
        else:
            return b

# Exercise 5
def sum_uniques(a: int, b: int, c: int) -> int:
    """Returns the sum of three integers (a,b,c).
    However if one of the integers is the same as another,
    it is not used when the sum is calculated.
    If all three integers are equal, the function returns 0.
    >>> sum_uniques(1,2,3)
    6
    >>> sum_uniques(1,1,3)
    3
    >>> sum_uniques(-1,1,2)
    2
    >>> sum_uniques(1,5,1)
    5
    >>> sum_uniques(4,1,1)
    4
    >>> sum_uniques(-4,-5,-6)
    -15
    """
    if a != b and b != c and c != a:
        return a + b + c
    elif a == b and c != a:
        return c
    elif a == c and b != a:
        return b
    elif c == b and a != b:
        return a
    else:
        return 0

def test_int(testing_string: str,expected:int, calculated: int) -> int:
    """
    Returns 1 if integer test passed, 0 otherwise.
    """
    print(testing_string)
    print("Expected Result: ",expected,"Actual Result: ",calculated)
    if expected == calculated:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0

def test_bool(testing_string: str,expected: bool, calculated: bool) -> int:
    """
    Returns 1 if boolean test passed, 0 otherwise.
    """
    print(testing_string)
    print("Expected Result: ",expected,"Actual Result: ",calculated)
    if expected == calculated:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0

#Main Script
#Testing Exercise 1
print("Exercise 1")
numPassed = 0
total_test = 0
numPassed += test_bool("bakers_party(39, True)",False,bakers_party(39, True))
total_test += 1
numPassed += test_bool("bakers_party(39, False)",False,bakers_party(39, False))
total_test += 1
numPassed += test_bool("bakers_party(50, True)",True,bakers_party(50, True))
total_test += 1
numPassed += test_bool("bakers_party(40, True)",True,bakers_party(40, True))
total_test += 1
numPassed += test_bool("bakers_party(40, False)",True,bakers_party(40, False))
total_test += 1
numPassed += test_bool("bakers_party(60, False)",True,bakers_party(60, False))
total_test += 1
numPassed += test_bool("bakers_party(50, False)",True,bakers_party(50, False))
total_test += 1
numPassed += test_bool("bakers_party(100, True)",True,bakers_party(100, True))
total_test += 1
numPassed += test_bool("bakers_party(100, False)",False,bakers_party(100, False))
total_test += 1
print(numPassed,"tests passed for exercise 1")
print(total_test-numPassed,"tests failed for exercise 1")
print()

#Testing Exercise 2
print("Exercise 2")
numPassed = 0
total_test = 0
numPassed += test_bool("squirrel_play(100, False)",False,squirrel_play(100, False))
total_test += 1
numPassed += test_bool("squirrel_play(100, True)",True,squirrel_play(100, True))
total_test += 1
numPassed += test_bool("squirrel_play(60, True)",True,squirrel_play(60, True))
total_test += 1
numPassed += test_bool("squirrel_play(70, False)",True,squirrel_play(70, False))
total_test += 1
numPassed += test_bool("squirrel_play(70, True)",True,squirrel_play(70, True))
total_test += 1
numPassed += test_bool("squirrel_play(60, False)",True,squirrel_play(60, False))
total_test += 1
numPassed += test_bool("squirrel_play(59, False)",False,squirrel_play(59, False))
total_test += 1
print(numPassed,"tests passed for exercise 2")
print(total_test-numPassed,"tests failed for exercise 2")
print()

#Testing Exercise 3
print("Exercise 3")
numPassed = 0
total_test = 0
numPassed += test_bool("great_42(-43, 85)",True,great_42(-43, 85))
total_test += 1
numPassed += test_bool("great_42(-43,-85)",True,great_42(-43,-85))
total_test += 1
numPassed += test_bool("great_42(43,-85)",False,great_42(43,-85))
total_test += 1
numPassed += test_bool("great_42(42,0)",True,great_42(42,0))
total_test += 1
numPassed += test_bool("great_42(-42,0)",True,great_42(-42,0))
total_test += 1
numPassed += test_bool("great_42(-100,12)",False,great_42(-100,12))
total_test += 1
numPassed += test_bool("great_42(-85,43)",False,great_42(-85,43))
total_test += 1
print(numPassed,"tests passed for exercise 3")
print(total_test-numPassed,"tests failed for exercise 3")
print()

#Testing Exercise 4
print("Exercise 4")
numPassed = 0
total_test = 0
numPassed += test_int("blackjack(19,20)",20,blackjack(19,20))
total_test += 1
numPassed += test_int("blackjack(19,21)",21,blackjack(19,21))
total_test += 1
numPassed += test_int("blackjack(17,22)",17,blackjack(17,22))
total_test += 1
numPassed += test_int("blackjack(23,25)",0,blackjack(23,25))
total_test += 1
numPassed += test_int("blackjack(14,17)",17,blackjack(14,17))
total_test += 1
print(numPassed,"tests passed for exercise 4")
print(total_test-numPassed,"tests failed for exercise 4")
print()

#Testing Exercise 5
print("Exercise 5")
numPassed = 0
total_test = 0
numPassed += test_int("sum_uniques(3,2,3)",2,sum_uniques(3,2,3))
total_test += 1
numPassed += test_int("sum_uniques(1,2,3)",6,sum_uniques(1,2,3))
total_test += 1
numPassed += test_int("sum_uniques(4,4,5)",5,sum_uniques(4,4,5))
total_test += 1
numPassed += test_int("sum_uniques(-1,-2,-3)",-6,sum_uniques(-1,-2,-3))
total_test += 1
numPassed += test_int("sum_uniques(-1,2,2)",-1,sum_uniques(-1,2,2))
total_test += 1
print(numPassed,"tests passed for exercise 5")
print(total_test-numPassed,"tests failed for exercise 5")

# Do not put any code below this line
print("End of file reached successfully.")
# Note that if this message isn not printed when you run your script, there is an error in your script.