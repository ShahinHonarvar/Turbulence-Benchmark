
def prime_factors(my_list):
    # Get the integer at index 40
    num = my_list[40]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # Check if the number is divisible by i
        if num % i == 0:
            # If it is, add i to the set of prime factors
            prime_factors.add(i)
    # Return the set of all prime factors of the integer at index 40
    return prime_factors
