def all_right_truncatable_prime(x):
    return [i for i in range(2, x) if all(x % i == 0 or x % i == i for j in range(2, int(str(x // i)) + 1)) and x % i == 0]
