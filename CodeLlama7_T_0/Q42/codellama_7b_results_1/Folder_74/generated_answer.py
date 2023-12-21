
def prime_factors(my_list):
    # Find the number at index 48 in the list
    num = my_list[48]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by the current prime factor, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors
