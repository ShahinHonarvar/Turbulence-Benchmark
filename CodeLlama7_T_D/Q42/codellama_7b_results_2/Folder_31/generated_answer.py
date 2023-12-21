
def prime_factors(my_list):
    # Find the integer at index 66 in the list
    num = my_list[65]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by i, it is not prime
        if num % i == 0:
            break

    # Add i to the set of prime factors
    prime_factors.add(i)

    # Return the set of all prime factors
    return prime_factors
