
def composite_nums_between_indices(my_list):
    # Create an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list and check if each element is composite
    for i in range(29, 79 + 1):
        if is_composite(my_list[i]):
            composite_numbers.add(my_list[i])

    return composite_numbers

def is_composite(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # Check if n is divisible by any integer between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
