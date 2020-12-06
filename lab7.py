#Lab 7
#Student: Adnan Hafeez 101210710

def factorial(n: int) -> int:
    """Return n! for positive values of n.
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    fact = 1
    for i in range(2,n+1):
        fact = fact * n
    return fact

def tip(cost: float, sat: int) -> float:
    """
    Returns the tip (in percent) based on the satisfaction level of the diner.
    :param cost: Cost of the meal, (float value)
    :param sat: Satisfication level. Integer 1: Totally Satisfied (20%), Integer 2 = Somewhat satisfied (15%). Integer 3 = Dissatisfied (5%).
    :return: Calculated tip (float) based on the cost of the meal and satisifcation rating.
    >>> tip(58.67,3)
    2.9335000000000004
    >>> tip(58.67,2)
    8.8005
    >>> tip(58.67,1)
    11.734000000000002
    """
    if sat == 1:
        return cost*0.20
    elif sat == 2:
        return cost*0.15
    else:
        return cost*0.05



def coupon(amount: float) -> float:
    """
    Returns the dollar amount automatically calculated based on the amount of grocery cost spent at the supermarket.
    If the cost is above 210$, coupon value is 14%, above 150$ its 12%, above 60$ its 10%, above 10$ its 8%, and below 10$ theres no coupon (0%)
    >>> coupon(250)
    35.0
    >>> coupon(180)
    21.599999999999998
    >>> coupon(76)
    7.6000000000000005
    >>> coupon(76.24)
    7.624
    >>> coupon(25)
    2.0
    >>> coupon(5)
    0
    """
    if amount > 210:
        #return value of coupon in dollars (amount)x(group percent)
        return amount*0.14
    elif amount > 150:
        return amount*0.12
    elif amount > 60:
        return amount*0.10
    elif amount > 10:
        return amount*0.08
    else:
        return 0


def test_int(testing_string: str,expected:int, calculated: int) -> int:
    """
    Returns the result of a function test, either 1 or 0. A testing functioned designed to automatically test integer values calculates vs. expected. Returns 1 if the test passed, and returns 0 if failed.
    >>> test_int("Testing factorial(1)",1,factorial(1))
    Testing factorial(1)
    Expected Result:  1 Actual Result:  1
    Test passed
    >>> test_int("Testing factorial(2)",2,factorial(2))
    Testing factorial(2)
    Expected Result:  2 Actual Result:  2
    Test passed
    >>> test_int("Testing factorial(3)",6,factorial(3))
    Testing factorial(3)
    Expected Result:  2 Actual Result:  9
    Test failed
    >>> test_int("Testing factorial(4)",24, factorial(4))
    Testing factorial(4)
    Expected Result:  24 Actual Result:  64
    Test failed
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

#Exercise 1
print("Exercise 1")
numPassed = 0
total_test = 0

numPassed += test_int("Testing factorial(1)",1,factorial(1))
total_test += 1

numPassed += test_int("Testing factorial(2)",2,factorial(2))
total_test += 1

numPassed += test_int("Testing factorial(3)",6,factorial(3))
total_test += 1

numPassed += test_int("Testing factorial(4)",24,factorial(4))
total_test += 1

print(numPassed,"tests passed for exercise 1")
print(total_test-numPassed,"tests failed for exercise 1")


#Exercise 2
print("Exercise 2")
test1 = tip(58.67,3) #dissatisifed customer, tips 5%, 5% of 58.67 is 2.9335 (Iphone Calculator)
test2 = tip(58.67,2) #somewhat satisfied customer, tips 15%, 5% of 58.67 is 8.8005 (Iphone Calculator)
test3 = tip(58.67,1) #totally satisified customer, tips 20%, 5% of 58.67 is 11.734 (Iphone Calculator)

numPassed = 0
numFailed = 0
print("Testing tip(58.67,3)")
print("Expected Result: 2.9335000000000004","Actual Result: ",test1)
if abs(test1 - (2.9335000000000004)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing tip(58.67,2)")
print("Expected Result: 8.8005","Actual Result: ",test2)
if abs(test2 - 8.8005) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing tip(58.67,1)")
print("Expected Result: 11.734000000000002","Actual Result: ",test3)
if abs(test3 - 11.734000000000002) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print(numPassed,"tests passed for exercise 2")
print(numFailed,"tests failed for exercise 2")


#Exercise 3
print("Exercise 3")
numPassed = 0
numFailed = 0
print("Testing coupon(250)")
print("Expected Result: 35.0","Actual Result: ",coupon(250))
if abs(coupon(250) - (35.0)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing coupon(180)")
print("Expected Result: 21.599999999999998","Actual Result: ",coupon(180))
if abs(coupon(180) - (21.599999999999998)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing coupon(76)")
print("Expected Result: 7.6000000000000005","Actual Result: ",coupon(76))
if abs(coupon(76) - (7.6000000000000005)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing coupon(76.24)")
print("Expected Result: 7.624","Actual Result: ",coupon(76.24))
if abs(coupon(76.24) - (7.624)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing coupon(25)")
print("Expected Result: 2.0","Actual Result: ",coupon(25))
if abs(coupon(25) - (2.0)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1

print("Testing coupon(5)")
print("Expected Result: 0","Actual Result: ",coupon(5))
if abs(coupon(5) - (0)) < 0.0001:
    print("Test passed")
    numPassed += 1
else:
    print("Test failed")
    numFailed += 1
print(numPassed,"tests passed for exercise 3")
print(numFailed,"tests failed for exercise 3")





# Do not put any code below this line
print("End of file reached successfully.")
# Note that if this message isn not printed when you run your script, there is an error in your script.
