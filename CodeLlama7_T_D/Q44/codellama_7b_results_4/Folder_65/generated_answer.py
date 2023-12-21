
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(82, 87):
        # Check if the current number is prime
        if my_list[i] == 1:
            continue

        # Check if the current number is composite by dividing it with all the numbers in the range [2, int(sqrt(my_list[i]))])
        for j in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % j == 0:
                composite_nums.add(my_list[i])
                break

    return composite_nums
