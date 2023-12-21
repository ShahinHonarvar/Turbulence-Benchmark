
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 10 or '0' in str(num):
            continue
        left_right_truncatable = True
        n = num
        while len(str(n)) > 2:
            if not is_prime(n):
                left_right_truncatable = False
                break
            n = int(str(n)[1:-1])
        if left_right_truncatable:
            primes.append(num)
    return sorted(primes)
