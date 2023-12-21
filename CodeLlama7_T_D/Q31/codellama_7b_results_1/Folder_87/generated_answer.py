
def if_perfect_num(my_list):
    # Check that the list is non-empty and has at least 96 elements
    if len(my_list) < 96:
        return False

    # Initialize a variable to store the sum of the factors of the number at index 96
    sum_of_factors = 0

    # Iterate over the factors of the number at index 96
    for factor in range(1, int(my_list[96] ** 0.5) + 1):
        if my_list[96] % factor == 0:
            sum_of_factors += factor

    # Return True if the sum of the factors is equal to the number at index 96, otherwise return False
    return sum_of_factors == my_list[96]
