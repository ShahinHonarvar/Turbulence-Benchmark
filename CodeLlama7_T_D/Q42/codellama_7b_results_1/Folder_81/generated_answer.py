
def prime_factors(my_list):
    # Find the number at index 20 in the list
    num = my_list[20]
    # Initialize an empty set to store the prime factors
    prime_factor_set = set()
    # Loop through all numbers less than or equal to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by the current number, add it to the prime factor set
        if num % i == 0:
            prime_factor_set.add(i)
    return prime_factor_set
