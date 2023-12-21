
def prime_factors(my_list):
    # Find the prime factor of the integer at index 51
    prime_factor = my_list[51]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through the divisors of the prime factor
    for i in range(2, int(prime_factor ** 0.5) + 1):
        # If the divisor is a prime number and it divides the prime factor without leaving a remainder, add it to the set of prime factors
        if prime_factor % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors

# Check if a number is prime by iterating from 2 to its square root and checking if it is divisible without leaving a remainder
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
