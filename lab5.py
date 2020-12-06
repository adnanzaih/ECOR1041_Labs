#Lab 5
#Student: Adnan Hafeez 101210710

#Exercise 1
def min_RRIF_widthdrawal(age: int, balance: float) -> float:
    """
    Returns the minimum RRIF widthdrawal amount (annual) for ages between 55 and 70 required by law.
    The first parameter is age (int), the second parameter is the balance (float) at the start of the year.

    :param age: An integer value, must be between 55 and 70 inclusive. Cannot be equal to 90.
    :param balance: A float value ($), the balance at the start of the year (the year when RRIF widthdrawal starts). Must be greater than zero.
    :return: The calculated minimum RRIF widthdrawal amount required.

    >>> min_RRIF_widthdrawal(55,10000.0)
    285.71
    >>> min_RRIF_widthdrawal(70,10000.0)
    500.0
    >>> min_RRIF_widthdrawal(65,0)
    0.0
    >>> min_RRIF_widthdrawal(69,125648.58)
    5983.26
    """
    return round(balance/(90-age),2)

#Exercise 2
def accrued_amount(principal: float, rate: float, compound: int, time: float) -> float:
    """
    Returns the accrued amount using the compound interest formula A = P(1 + r/n)^(nt), using Principal(R), rate(r), compounding periods (n), and years (t).
    :param principal: The Principal Amount (float). Must be greater than or equal to zero.
    :param rate: Annual Nominal Interest rate in percent. Must be greater than zero.
    :param compound: number of compounding periods per unit of time. Must be greater than zero.
    :param time: Time involved in years, 0.5 years is calculated as 6 months. Must be greater than zero.
    :return: The calculated accrued amount using the compound interest formula.

    >>> accrued_amount(10000,6,1,1)
    10600.0
    >>> accrued_amount(10000,0.1,365,10)
    10100.50
    >>> accrued_amount(10000,6,12,1)
    10616.78
    >>> accrued_amount(0,6,1,1)
    0.0
    """
    return round(principal*(1+(rate/100)/compound)**(time*compound),2)

#Exercise 1 Test Cases and Examples
help(min_RRIF_widthdrawal)
print(min_RRIF_widthdrawal(55,10000.0))
print(min_RRIF_widthdrawal(70,10000.0))
print(min_RRIF_widthdrawal(65,0))
print(min_RRIF_widthdrawal(69,125648.58))

#Exercise 2 Test Cases and Examples
print("RRIF Testing...")
print(accrued_amount(10000,6,1,1)) #10600.0 vs. (Online Compound Interest Calculator): 10,600.00
print(accrued_amount(10000,0.1,365,10)) #10100.501532478214 vs. (Online Compound Interest Calculator): 10,100.50
print(accrued_amount(10000,6,12,1)) #10616.778118644983 vs. (Online Compound Interest Calculator): 10,616.78
print(accrued_amount(0,6,1,1)) #0.0 vs. (Online Compound Interest Calculator): "Enter values greater than 0", the online calculator doesn't work for principal of 0$




# Do not put any code below this line
print("End of file reached successfully.")
# Note that if this message isn not printed when you run your script, there is an error in your script.