
def prime_factors(my_list):
    # Check if input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Find the prime factors of the integer at index 2
    prime_factors = set()
    for i in range(2, my_list[2] + 1):
        if my_list[2] % i == 0:
            prime_factors.add(i)
    return prime_factors
