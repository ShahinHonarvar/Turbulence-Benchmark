
def composite_nums_between_indices(my_list):
    # Define the range of indices to check
    start_index = 527
    end_index = 538
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the elements in the given list within the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] > 1:
            # Check if the element is divisible by any of its proper divisors
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    break
            else:
                # If the element is not divisible by any of its proper divisors, it is a composite number
                composite_numbers.add(my_list[i])

    return composite_numbers
