
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[1]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            num = str(n)
            is_right_truncatable = True
            while len(num) > 1:
                num = num[:-1]
                if not is_prime(int(num)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)
