
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            number = str(i)
            is_truncatable_prime = True
            for j in range(1, len(number)):
                if not is_prime(int(number[:-j])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
