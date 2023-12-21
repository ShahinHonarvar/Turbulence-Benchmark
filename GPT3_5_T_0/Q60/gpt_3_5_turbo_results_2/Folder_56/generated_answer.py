
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 23:
            continue
        for i in range(2, x):
            if not is_prime(i):
                continue
            s = str(i)
            if '0' in s:
                continue
            truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:j])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)
