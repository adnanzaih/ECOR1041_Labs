#Lab 4
#Student: Adnan Hafeez 101210710

import math

def area_of_disk(radius):
    return math.pi * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
    return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg

def accumulated_amount(principal, rate, n, time):
    '''
    amount: amount of money after time years
    #principal is the initial amount of money
    #rate is the rate of interest, specified in decimal
    #n is num of times interested is compounded
    #time is in years
    '''
    return principal * pow(1+rate/n,n*time)

def area_of_cone(height, radius):
    '''
    calculates and returns the lateral surface area of right circular cone
    Given height and radius > 0
    '''
    return math.pi * radius * math.sqrt(radius**2 + height**2)


#Main Script

#Exercise 1
area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

#Exercise 2
litres_per_100km = convert_to_litres_per_100_km(32)
print("Exercise 2: 32 mpg =", convert_to_litres_per_100_km(32),"1/100 km")
#prints Exercise 2: 32 mpg = 8.8275512011135 1/100 km

#litres_per_100km = convert_to_litres_per_100_km(0) will return an error
print('no return value, zero division error')
#the above statement causes float division by zero error, we cannot divide by zero,
# The function attempts to divide by mpg which we assigned to zero.
# In order to avoid a python error, we have commented this particular line.

litres_per_100km = convert_to_litres_per_100_km(32.0) # 8.8275512011135

print("Exercise 2: 32.0 mpg =", convert_to_litres_per_100_km(32.0),"1/100 km")
#prints Exercise 2: 32 mpg = 8.8275512011135 1/100 km

print("Exercise 2: 37.0 mpg =", convert_to_litres_per_100_km(37.0),"1/100 km")
#prints Exercise 2: 37.0 mpg = 7.634638876638704 1/100 km

print("Exercise 2: 5.0 mpg =", convert_to_litres_per_100_km(5.0),"1/100 km")
#prints Exercise 2: 5.0 mpg = 56.4963276871264 1/100 km

#The above assignment and print line statements shows that the convert_to_litres_per_100_km() function
# correctly converts mpg to litres...
# even if the input argument is a float

#Exercise 3
#for principal = 1500$, interest rate = 4.3%, compounded = 4, years = 6
print(accumulated_amount(1500,4.3/100, 4, 6)) # 1938.8368221341054

#for principal = 100$, interest rate = 4.3%, compounded = 1, years = 3
print(accumulated_amount(100,4.3/100, 1, 3)) # 113.46265069999997

#for principal = 100$, interest rate = 5%, compounded = 5, years = 5
print(accumulated_amount(10000,5/100, 5, 5)) # 12824.319950172337

#boundary value testing, we divide the interest rate by 100 in the argument to convert it to decimal form.
#for principal = 0$, interest rate = 5%, compounded = 1, years = 5
print(accumulated_amount(0,5/100, 1, 5)) # 0

#for principal = 100$, interest rate = 0%, compounded = 5, years = 5
print(accumulated_amount(100,0/100, 5, 5)) # 100.0

#for principal = 100$, interest rate = 5.5%, compounded = 0, years = 5
#print(accumulated_amount(100,5.5/100, 0, 5)) # ZeroDivisionError
#the above line gives a zero division error because it tries to divide rate by zero.

#for principal = 100$, interest rate = 4%, compounded = 1, years = 0
print(accumulated_amount(100,4/100, 5, 0)) # 100.0

#for principal = 100$, interest rate = 0%, compounded = 1, years = -5
print(accumulated_amount(100,0/100, 5, -5)) # 100.0

#for principal = 100$, interest rate = 5%, compounded = -5, years = -5
print(accumulated_amount(100,5/100, -5, -5)) # 77.78213593991467

#Exercise 4
#first argument = height, second argument = radius
print(area_of_cone(5,5)) #testing h = 5, r = 5, area = 111.07207345395915
#testing boundary case when height is zero
print(area_of_cone(0,5)) #testing h = 0, r = 5, area = 78.53981633974483, area of 2D circle

#testing another edge case when radius is zero
print(area_of_cone(5,0)) #0, makes sense if radius = 0

#testing to see if negative numbers work, in this case the formula is only valid for positive, but negative number's don't produce any errors, just a bug.
print(area_of_cone(-10,5)) #175.62036827601816

#testing float variables and negative numbers..
print(area_of_cone(-10,5.0)) #h = -10, r = 5.0, area = 175.62036827601816, testing floats




# Do not put any code below this line
print("End of file reached successfully.")
# Note that if this message isn not printed when you run your script, there is an error in your script.