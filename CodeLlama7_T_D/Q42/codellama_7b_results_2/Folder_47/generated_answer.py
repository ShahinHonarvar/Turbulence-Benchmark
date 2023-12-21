
def prime_factors(my_list):
    # Check if input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Get the prime factors of the integer at index 34
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % j == 0:
                prime_factors.add(j)
    return prime_factors
