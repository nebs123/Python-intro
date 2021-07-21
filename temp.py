# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = '1.23,2.4,3.123'
sum = 0.0
temp = ''
for x in s:
    
    if x == ',':
        sum += float(temp)
        temp = ''
    else:
        temp +=x 

print(sum + float(temp))

#Bisection search for square root
x = 24
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans) 
    numGuesses += 1
    if ans**2 < x:
        low = abs(ans)
    else:
        high = abs(ans)
    ans = (high + low)/2.0
print('numGuesses =', numGuesses) 
print(round(ans, 3), 'is close to square root of', x)


#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0 epsilon = 0.01
k = 24.0
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess)) 
    numGuesses += 1
print('Square root of', k, 'is about', round(guess,3))
print("Number of guesses is", numGuesses)


#Binary searches for val in ordered list array
def binary_search(array, val):
    
    '''
    array: list of ordered numbers
    val: value to be seearched
    @return number of guess or -1 if value not found
    '''
    low = 0 
    high = len(array) - 1
    guess = (low + high) // 2
    
    while low <= high and array[guess] != val:
        if array[guess] < val:
            low = guess + 1
        else:
            high = guess - 1
        
        guess = (low + high) // 2
        
    if low <= high:
        return guess
    else:
        return -1


test = range(2**31 -1)
print(binary_search(test, 2**31 - 2))



#Finger excerciise
def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    
    sum=0
    for x in s:
        try:
            sum += int(x)
        except ValueError:
            continue
    
    return sum



def findAnEven(L):
    """
    

    Parameters
    ----------
    L : List
        List of numbers(float and int).

    Raises
    ------
    ValueError
        If none of the inputs in L is an integer.

    Returns
    -------
     int
        The first integer encoutered in L.

    """
    for x in L:
        try:
            assert type(x)== int, "found a non-int value"
            if x % 2 == 0:
                return x
            
        except TypeError:
            print("Input", x , "is not an integer")
    
    raise ValueError("No integer was found")
    
