
def prime_factors(my_list):
    # Check if input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the prime factors of the integer at index 92
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i] ** 0.5) + 1):
            if my_list[i] % j == 0:
                prime_factors.add(j)
    return prime_factors
