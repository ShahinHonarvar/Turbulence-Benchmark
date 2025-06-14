
def prime_factors(my_list):
    # Check if input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Find the prime factors of the first element in the list
    prime_factors = set()
    while my_list[0] != 1:
        if my_list[0] % 2 == 0:
            my_list[0] //= 2
        else:
            for i in range(3, int(my_list[0] ** 0.5) + 1, 2):
                if my_list[0] % i == 0:
                    prime_factors.add(i)
                    my_list[0] //= i
    return prime_factors
