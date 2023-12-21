
def prime_factors(my_list):
    # Get the integer at index 20
    num = my_list[20]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the number
    for i in range(1, num + 1):
        # If the number is divisible by the current divisor, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors
