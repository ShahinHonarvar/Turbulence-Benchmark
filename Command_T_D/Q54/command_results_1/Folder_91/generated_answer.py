def all_right_truncatable_prime(tup):
    return sorted(tup[0]//10**(10*i) for i in range(1, int(math.log(tup[0], 10**9) + 1)) if all(x % 10**(10*i) == 0 or x % 10**(10*i) == 5 or x % 10**(10*i) == 3 or x % 10**(10*i) == 7 for x in range(1, int(math.log(tup[0], 10**9) + 1)))
