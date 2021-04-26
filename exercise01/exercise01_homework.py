"""
exercise01
Wenjie Wu
Dong Zhang
"""

import unittest


# homework problem 1
def odd_fibonacci_numbers(n_numbers):
    """
    Return a list of the first N odd fibonacci numbers
    """
    '''
    We can see that only odd number + even number = odd number
    (odd + odd = even, even + even = even)
    recall for fibonacci seq. n = 1, 2 x_1, x_2=1,1 both odd
    so x_3 is a even number and due to
    x_n = x_(n-1) + x_(n-2),
    we find x_4 is odd, x_5 is odd, x_6 is even, x_7 is odd ...
    finally, we find that we can decompose the whole seq into
    (odd, odd, even) tuple.
    So for first n_numbers odd terms we need to compute N terms
    1. if n_numbes % 2 == 0, we need to compute
       N = (n_numbers // 2) * 3 terms
    2. else we need to compute
       N = (n_numbers // 2 + 1) * 3 terms
    then for n-th term x_n, if n%3 == 1 or 2, x_n is odd
    else x_n is even (actually n%3 can only be 0, 1, 2)
    '''
    res = []
    # #fibnacci number we need to compute
    N = 0
    if n_numbers % 2 == 0:
        N = (n_numbers // 2) * 3
    else:
        N = (n_numbers // 2 + 1) * 3
    fibs = fibonacci_seq_n(N)
    for n in range(1, N+1):
        if not n % 3 == 0:
            res.append(fibs[n-1])
    # if n_numbers % 2 != 0, we actually have one more term
    return res[:n_numbers]


# Optionally: Use a helper function that returns fibonacci numbers and use that
# in your main function that calculates the odd fibonacci numbers
# I do not use it. Because compute N-th term should be compute all
# terms before N but we still need terms before it
def nth_fibonacci_number(number):
    """
    Helper function that return nth fibonacci number
    """
    pass


# My help function
def fibonacci_seq_n(number):
    """
    return a list of fibonacci seq. contains `number` terms
    """
    if number == 1:
        return [1]
    if number == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, number):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# homework problem 2  ---------------------------------------------------------
# (a) ------------------------------------------------------------------------
def sum_square_difference(numbers):
    a = 0
    # initial value of ∑(x_n²)
    b = 0
    # initial value of (∑x_n)²

    for i in range(len(numbers)):
        a = a + (numbers[i])*(numbers[i])
        # ∑(x_n²)
        b = b + numbers[i]
        # (∑x_n)

    return a - (b*b) # ∑(x_n²) - (∑x_n)²

#print(sum_square_difference([1,2,3]))

#(b) ------------------------------------------------------------------------------------------------------------------------------------
def func_square_difference(func, numbers): # the variable of "func()" is list, so a and b are list now. 
    a = [] # add terms like x_n² to this list
    b = numbers # equal to the list "numbers"

    for i in range(len(numbers)):
        a = a + [(numbers[i])*(numbers[i])] # list of x_n²
        
    return func(a) - (func(b)*func(b)) # func(x_1²...x_n²) - func(x_1...x_n)² = func([x_1²,...,x_n²]) - func([x_1,...,x_n])²


#print(func_square_difference(mean, [1,2,3]))

#(c) ------------------------------------------------------------------------------------------------------------------------------------
def mean(numbers): # if "numbers" means a list, then it can be used, otherwise its useless.
    return sum(numbers)/len(numbers) # get the mean



def variance(numbers): # get the variance by setting func = mean
    return func_square_difference(mean, numbers)


if __name__ == '__main__':
    unittest.main(module="test_exercise01_homework", verbosity=2)
