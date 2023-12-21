
def prime_factors(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise TypeError("Input must be a list of integers")
    # Find the prime factors of the integer at index 845
    result = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) ** 0.5 + 1):
            if my_list[i] % j == 0:
                result.add(j)
                break

    return result
