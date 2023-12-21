
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the specified range
    first_index = 29
    last_index = 93
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each number is composite
    for i in range(first_index, last_index + 1):
        if is_composite(my_list[i]):
            composite_numbers.add(my_list[i])

    return composite_numbers

def is_composite(n):

    # Check if 'n' is divisible by 2 to 10
    for i in range(2, 11):
        if n % i == 0:
            return False

    return True
