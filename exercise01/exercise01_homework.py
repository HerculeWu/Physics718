"""
Template for the homework of exercise sheet 01.

Remember to run the tests (just run the file) to see if your solution is
correct.
"""

import unittest

# if you want you can re-use the is_odd function from the attendance exercise
# No, actually we don't need it
# from exercise01_attendance import is_odd


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


# homework problem 2
def sum_square_difference(numbers):
    """
    Return ∑(x_1²) - (∑x_n)²
    """
    # list for x_n**2
    numbers_sq = [x*x for x in numbers]
    # sum for x_n and x_n^2
    sum_x, sum_x_sq = 0.0, 0.0
    for x, x_sq in zip(numbers, numbers_sq):
        sum_x += x
        sum_x_sq += x_sq
    return sum_x_sq - (sum_x**2)


def func_square_difference(func, numbers):
    """
    Return func(x_1²...x_n²) - func(x_1...x_n)²

    :param func: And aggregating function that takes a list and returns a scalar number.
    """
    # List of [x_1^2...x_n^2]
    numbers_sqrt = [x*x for x in numbers]
    return func(numbers_sqrt) - (func(numbers)**2)


def mean(numbers):
    "Calculates the arithmetic mean of ``numbers``"
    return sum(numbers) / len(numbers)


def variance(numbers):
    "Calculates the variance of ``numbers``"
    numbers_sq = [x*x for x in numbers]
    # mean for x_n and x_n^2
    ev, ev_2 = 0.0, 0.0
    for x, x_sq in zip(numbers, numbers_sq):
        ev += x
        ev_2 += x_sq
    # length of numbers
    N = len(numbers)
    ev /= N
    ev_2 /= N
    return ev_2 - (ev*ev)


if __name__ == '__main__':
    unittest.main(module="test_exercise01_homework", verbosity=2)
