
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[630]
    truncatable_primes = []
    for num in range(x-1, 1, -1):
        if '0' not in str(num):
            stripped = str(num)
            is_truncatable_prime = True
            while stripped:
                if not is_prime(int(stripped)):
                    is_truncatable_prime = False
                    break
                stripped = stripped[1:]
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return truncatable_primes
