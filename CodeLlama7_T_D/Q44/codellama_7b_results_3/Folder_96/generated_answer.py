
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(60, 201):
        # Check if the current element is divisible by any number between 2 and its square root
        for j in range(2, int(i ** 0.5) + 1)):
            if i % j == 0:
                composite_nums.add(i)
                break

    return composite_nums
