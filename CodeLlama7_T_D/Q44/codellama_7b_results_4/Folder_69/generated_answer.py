
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list from index 29 to 79 (inclusive)
    for i in range(29, 80):

        # Check if the current element is divisible by any of the prime factors of its neighbors
        if all(my_list[i] % my_list[j] != 0 for j in range(max(0, i - 1), min(len(my_list), i + 1)))):

            # If it is divisible by no prime factors, it is a composite number
            composite_numbers.add(my_list[i])

    return composite_numbers
