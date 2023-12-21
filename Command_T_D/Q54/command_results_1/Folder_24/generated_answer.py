def all_right_truncatable_prime(n):
    # add your code here
    # sort by digit and length and filter by digit and length
    # list comprehension
    return sorted(list(set(str(x) for x in range(2, n[0] + 1) if all(x % 10**i == 0 for i in range(1, len(str(x)) + 1))))
