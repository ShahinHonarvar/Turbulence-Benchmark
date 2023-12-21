
def prime_factors(my_list):
    # Find the number at index 790 in the list
    num = my_list[790]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by the current value of i, it is not prime
        if num % i == 0:
            break

    # Add the number to the set of prime factors
    prime_factors.add(num)

    return prime_factors
