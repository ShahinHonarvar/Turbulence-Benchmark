
def prime_factors(my_list):
    # Check if input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the integer at index 2
    n = my_list[2]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Loop through all numbers from 2 to n-1
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            # Add i to the set of prime factors
            prime_factors.add(i)
    return prime_factors
