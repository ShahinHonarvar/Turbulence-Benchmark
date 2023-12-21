
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
        for i in range(2, int(x**0.5) + 1):
            if not is_prime(i):
                continue
            s = str(i)
            if s[-1] != '3' and s[-1] != '7':
                continue
            truncatable = True
            while len(s) > 1:
                s = s[1:-1]
                if not is_prime(int(s)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)
