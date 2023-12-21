
def prime_factors(my_list):
    # Check if input is a list of integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Find the prime factors of the integer at index 3
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        while my_list[i] % 2 == 0:
            my_list[i] //= 2
        prime_factors.add(my_list[i])
    return prime_factors
