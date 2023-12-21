
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the indices in the given range
    for i in range(25, 60):
        # Check if the current number is prime
        if my_list[i] == 1:
            continue

        # Iterate from the current number to its square root
        for j in range(my_list[i], int(math.sqrt(my_list[i])) + 1):
            # Check if the current number is divisible by any number in the given list
            if any(my_list[i] % x == 0 for x in my_list[j:]):
                composite_nums.add(my_list[i])
                break

    return composite_nums
