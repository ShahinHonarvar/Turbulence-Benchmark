
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 10:
            continue
        if is_prime(x):
            s = str(x)
            truncatable = True
            for i in range(1, len(s)):
                if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(x)
    primes.sort(reverse=True)
    return primes
