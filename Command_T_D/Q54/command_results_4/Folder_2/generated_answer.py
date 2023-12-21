import sys
import heapq
def all_right_truncatable_prime(test_case):
    return heapq.nlargest(test_case[618], list(test_case))
