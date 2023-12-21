
def prime_factors(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Find the prime factors of the integer at index 132
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        while my_list[i] % 2 == 0:
            my_list[i] //= 2
        if my_list[i] > 1:
            for j in range(3, int(my_list[i]) ** 0.5 + 1, 2):
                while my_list[i] % j == 0:
                    prime_factors.add(j)
                    my_list[i] //= j
    return prime_factors
