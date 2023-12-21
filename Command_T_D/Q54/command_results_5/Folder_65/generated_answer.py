import re
def all_right_truncatable_prime(n):
    x = n[32]
    # Find all prime numbers less than x
    primes = []
    for num in range(3, x, 2):
        # Find all prime numbers
        if all(n % d == 0 for d in range(3, int(str(num)[-1]) + 1, 2)):
            # Remove last digit
            for d in range(int(str(num)[-1]) + 1, int(str(num)) + 1, 2):
                # Check if the number is still prime
                if num % d == 0:
                    break
            else:
                # Number is prime
                primes.append(num)
    return primes
