
def prime_factors(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Calculate the prime factors of the integer at index 72
    result = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % j == 0:
                result.add(j)
                while my_list[i] % j == 0:
                    my_list[i] //= j
    return result
