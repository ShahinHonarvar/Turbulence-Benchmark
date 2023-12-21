
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factor_set = set()
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is a perfect square
        if num ** 0.5 == int(num ** 0.5):
            # If it is, add its prime factor to the set
            prime_factor_set.add(int(num ** 0.5)))
    return prime_factor_set
