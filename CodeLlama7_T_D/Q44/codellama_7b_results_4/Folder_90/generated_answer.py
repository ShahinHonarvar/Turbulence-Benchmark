
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list of positive integers
    for i in range(333, 369):
        # Check if the current number is divisible by any number between 2 and its square root
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(i)
    return composite_nums
