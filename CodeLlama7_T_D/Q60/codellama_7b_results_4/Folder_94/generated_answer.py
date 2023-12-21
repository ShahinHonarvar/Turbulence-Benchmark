
def all_left_right_truncatable_prime(x):
    if x < 2: return []
    prime_numbers = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: continue
        s = str(x)
        if s[:-i] == s[i:] and s[:-i][:-1] != '':
            prime_numbers.append(int(s))
    return sorted(prime_numbers)
