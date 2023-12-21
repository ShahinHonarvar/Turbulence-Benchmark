
def prime_factors(my_list):
    # Get the integer at index 48
    num = my_list[48]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # If num is divisible by i, it is not prime
        if num % i == 0:
            break

    # Add i to the set of prime factors
    prime_factors.add(i)
    # Return the set of all prime factors of num
    return prime_factors
