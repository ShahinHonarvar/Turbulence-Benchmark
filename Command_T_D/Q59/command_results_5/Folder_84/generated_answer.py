def all_left_truncatable_prime(n):
    return sorted(set(str(n)[0] + str(x) for x in range(2, int(str(n)[0]) + 1) if all(str(x)[i] != '0' for i in range(1, len(str(x)) + 1)) and all(str(x)[0] * 10**(len(str(x)) - i - 1) % 9 + str(x)[i + 1] not in '2357' for i in range(1, len(str(x)) + 1)), reverse=True)
