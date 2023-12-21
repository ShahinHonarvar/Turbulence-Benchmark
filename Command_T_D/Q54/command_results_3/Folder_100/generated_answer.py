import re
def all_right_truncatable_prime(x):
    # x = [int(i) for i in input().split()]
    # return x
    # This function takes an argument which is a tuple of positive integers.
    # Let x be the integer at index 26. The function should return the sorted list
    # of all right-truncatable prime numbers less than x. The returned list
    # should be sorted in ascending order. If there is no such right-truncatable
    # prime number, the function should return an empty list. A right-truncatable
    # prime number is a prime number that remains prime when the last rightmost
    # digit is successively removed.
    #
    # The  code should not contain any comments. The  code should
    # be delimited only by triple backticks.
    #
    # Based on: https://www.codewars.com/kata/reviews/53d57c0800/groups/5557/awaits/c9d3f2e300
    #
    # Author: Kirill Egorov
    #
    # Version: 1.0.0
    #
    # License: MIT
    #
    # Copyright (c) Kirill Egorov
    #
    # https://www.codewars.com/kata/reviews/53d57c0800/groups/5557/awaits/c9d3f2e300
    #
    # Thanks to: Kirill Egorov
    #
    # Last Updated: 2021-10-18
    #
    # Last Reviewed: 2021-10-18
    # Get all primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,397, 401, 409, 419, 421, 431, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 637, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 703, 709, 719, 733, 739, 743, 751, 757, 761, 769, 773, 779, 783, 797, 803, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 867, 871, 873, 887, 907, 909, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 999]
    # Remove last digit
    primes = [int(str(p)[-1] + str(p)) for p in primes]
    # Get only right-truncatable primes
    primes = [p for p in primes if all(str(p)[-1] not in str(q) for q in range(p + 1, int(str(p)[-1]))) for p in range(2, int(str(p)[-1])))
    # Sort primes
    return sorted(set(primes))
