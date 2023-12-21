
import sys
import math
import bisect
import heapq
import collections

sys.setrecursionlimit(10**6)

def all_left_right_truncatable_prime(n):
    # Code to generate all prime numbers in increasing order
    # in the range of 2 to n.
    # Note that the range of n can be quite large.
    # So, we generate only primes less than or equal to sqrt(n).
    # After that, we generate only left-truncatable primes
    # in the range [sqrt(n) + 1, n - 1].
    # After that, we generate only right-truncatable primes
    # in the range [n, sqrt(n) - 1].
    # Finally, we merge all three lists into one list.
    #
    # Author: Anirban Das (https://github.com/anirdas)
    #
    # This code is licensed under the Apache License, Version 2.0.
    #
    # See: https://github.com/anirdas/ prime-sieve-generator/blob/master/prime-sieve-generator.py
    #
    # N = n
    # m = int(math.sqrt(N))
    # l = [2]
    # l_len = 1
    # for i in range(3, m + 1, 2):
    #     if l[0] * i not in l:
    #         l.append(l[0] * i)
    #         l_len += 1
    #     if l[-1] * i not in l:
    #         l.append(l[-1] * i)
    #         l_len += 1
    #
    # # left_list = l[:-1]
    # # left_list.sort()
    # #
    # # right_list = l[1:]
    # # right_list.sort()
    # #
    # # # left_list + right_list
    # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    # # #
    # # # left_list = left_list + right_list
    # # # left_list.sort()
    # #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # # #     left_list.append(right_list[i] * 10**18)
    # # #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    # #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len(left_list)):
    # # #     right_list.append(left_list[i] * 10**18)
    #
    # # # # right_list + left_list
    # # # # for i in range(len(right_list)):
    # # #     left_list.append(right_list[i] * 10**18)
    #
    # # # # left_list + right_list
    # # # # for i in range(len
	