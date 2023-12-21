import itertools
def all_left_truncatable_prime(n):
    # your code here
    lst = [int(i) for i in range(2, n[0]) if all(str(i).rstrip('0') in str(j) for j in range(i, n[0] + 1, i))]
    return sorted(lst)
