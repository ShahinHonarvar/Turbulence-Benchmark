
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for i in range(2, x+1):
        if '0' in str(i):
            continue
        s = str(i)
        is_truncatable = True
        while len(s) > 1:
            if not is_prime(int(s)):
                is_truncatable = False
                break
            s = s[1:-1]
        if is_truncatable:
            primes.append(i)
    return primes
