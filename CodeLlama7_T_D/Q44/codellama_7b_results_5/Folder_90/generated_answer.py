
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(333, 368 + 1):
        # Check if the number is divisible by any number between 2 and its square root
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(i)
                # Break out of the inner loop since we have found a factor
                break

    return composite_nums
