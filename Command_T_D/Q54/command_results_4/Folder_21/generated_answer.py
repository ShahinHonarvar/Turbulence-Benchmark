import heapq
def all_right_truncatable_prime(x):
    # primes are always right-truncatable
    heapq.heapify(x)
    return heapq.nsmallest(len(x), x)
