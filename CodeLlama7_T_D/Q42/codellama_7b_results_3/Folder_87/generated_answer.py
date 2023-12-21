
def prime_factors(my_list):
    # Find the number at index 96 in the list
    number = my_list[96]
    # Initialize an empty set to store the prime factors
    prime_factor_set = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by the current prime factor, add it to the set
        if number % i == 0:
            prime_factor_set.add(i)
    return prime_factor_set
