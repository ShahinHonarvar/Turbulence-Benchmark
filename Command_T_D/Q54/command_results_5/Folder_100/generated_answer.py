def all_right_truncatable_prime(n):
    return [n for n in range(2, int(str(n)[-1]))) if all(str(n)[-1] != d or n == int(str(n)[0] + str(d))) for d in range(2, str(n)[-1])]
