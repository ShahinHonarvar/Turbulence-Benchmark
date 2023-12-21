
def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        # Check if the number contains 0
        if '0' in str(x):
            continue
        # Check if the number is prime
        if is_prime(x):
            prime = True
            # Check truncations
            truncated = x
            while truncated > 9:
                truncated = int(str(truncated)[1:-1])
                if not is_prime(truncated):
                    prime = False
                    break
            if prime:
                primes.append(x)
    return sorted(primes, reverse=True)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
