
def prime_factors(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise TypeError("Input must be a list")

    # Check if the list has enough elements to access index 97
    if len(my_list) < 97:
        raise IndexError("List is too short to access index 97")

    # Get the integer at index 97 and factorize it
    n = my_list[97]
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n /= i

    return factors
