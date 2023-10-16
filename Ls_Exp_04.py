"""
    Write a python program to compute future of the specify principle amount ,rate of interest and number of years.
    The formula for future value with compound interest is FV=P(1+r/n)^nt
    Where,
    FV = future value
    P = principle
    R = annual interest rate express as decimal
    N = number of time interest is paid each year
    T = time in year
    Amount = 10000
    Interest = 3.5
    Year = 7
"""
principal = 10000  
annual_interest_rate = 0.035  # Annual interest rate 3.5% expressed as a decimal
compounding_frequency = 1  
years = 7  

# Calculate the future value
future_value = principal * (1 + annual_interest_rate / compounding_frequency)**(compounding_frequency * years)
print(future_value)

"""
    Write a program to solve (x+y)*(x+y)
"""
x = 5
y = 4

result = (x + y) * (x + y)
print(result)
