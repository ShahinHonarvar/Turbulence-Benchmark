
def prime_factors(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(my_list) == 0:
        raise ValueError("List cannot be empty")
    # Get the integer at index 24
    n = my_list[24]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Add i to the set of prime factors
            prime_factors.add(i)
    return prime_factors
