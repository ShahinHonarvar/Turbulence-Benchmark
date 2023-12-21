
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list and check if each number is composite
    for i in range(686, 987 + 1):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_numbers
