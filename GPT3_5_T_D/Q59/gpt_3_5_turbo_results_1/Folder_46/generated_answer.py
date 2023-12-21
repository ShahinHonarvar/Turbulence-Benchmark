
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []

    for i in range(11, x):
        if not '0' in str(i):
            is_truncatable_prime = True
            truncations = str(i)

            while len(truncations) > 1:
                truncations = truncations[1:]
                if not is_prime(int(truncations)):
                    is_truncatable_prime = False
                    break

            if is_truncatable_prime:
                truncatable_primes.append(i)

    return truncatable_primes
