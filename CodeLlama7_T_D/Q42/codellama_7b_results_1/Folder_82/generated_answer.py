
def prime_factors(my_list):
    # Get the integer at index 83
    num = my_list[83]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the number
    for i in range(1, num + 1):
        # If the current divisor is a prime factor, add it to the set
        if num % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors

# Check if a number is prime by dividing it only by its factors up to its square root
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
