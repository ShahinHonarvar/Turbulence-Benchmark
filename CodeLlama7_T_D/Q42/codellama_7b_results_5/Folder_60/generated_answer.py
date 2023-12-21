
def prime_factors(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Invalid input")

    # Find the prime factors of the integer at index 88
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i] ** 0.5) + 1):
            if my_list[i] % j == 0:
                prime_factors.add(j)
                break

    return prime_factors
