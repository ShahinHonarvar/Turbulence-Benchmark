
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 10:
            continue
        s = str(x)
        if '0' in s:
            continue
        is_truncatable = True
        for i in range(len(s)):
            trunc_left = s[i:]
            trunc_right = s[:len(s)-i]
            if not is_prime(int(trunc_left)) or not is_prime(int(trunc_right)):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(x)
    return sorted(primes, reverse=True)
