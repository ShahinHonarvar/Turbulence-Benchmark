
def prime_factors(my_list):
    # Check if input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise TypeError("Input must be a list of integers.")
    # Get the first element of the list and find its prime factors
    prime_factors = set()
    for i in range(2, int(my_list[0]) + 1):
        if my_list[0] % i == 0:
            prime_factors.add(i)
    return prime_factors
