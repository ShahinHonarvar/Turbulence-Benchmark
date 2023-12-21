import itertools
def all_right_truncatable_prime(n):
    for i in range(3, int(str(n)[-1]) + 1):
        for j in range(10):
            if str(i**10**(j + 1))[-1] == str(n)[-1]:
                return [i**10**j]
    return []
