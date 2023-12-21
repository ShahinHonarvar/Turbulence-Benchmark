
def prime_factors(my_list):
    # Check if the input is a list of positive integers
    if not all([isinstance(x, int) and x > 0 for x in my_list])):
        raise ValueError("Input must be a list of positive integers")
    # Calculate the prime factors of the integer at index 990
    result = set()
    for i in range(len(my_list)):
        if i == 990:
            for factor in my_list[i]:
                if isprime(factor):
                    result.add(factor)
    return result
