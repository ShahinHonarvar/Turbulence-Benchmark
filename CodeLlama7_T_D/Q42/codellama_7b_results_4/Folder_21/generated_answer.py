
def prime_factors(my_list):
    # Get the integer at index 410
    num = my_list[410]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate through the divisors of the number
    for i in range(1, int(num ** 0.5) + 1):
        # If the number is divisible by the current divisor, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors
