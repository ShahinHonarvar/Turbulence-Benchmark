
def all_left_right_truncatable_prime(x_tuple):
    x, l = x_tuple
    primes = []
    for n in range(2, x // 2):
        s = str(n)
        if len(s) == 1:
            continue
        if s[0] != '0':
            if all(int(s[i]) for i in range(1, len(s) - 1)):
                if all(s[i] != '0' for i in range(len(s) - 2, -1, -1)):
                    primes.append(n)
    return sorted(primes)
