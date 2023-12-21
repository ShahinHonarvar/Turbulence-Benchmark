
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(10, 100 + 1):
        # Check if the current index is a prime number
        if my_list[i] == 1:
            continue

        # Check if the current index is a composite number
        for j in range(2, my_list[i] // 2 + 1):
            if my_list[i] % j == 0:
                composite_nums.add(my_list[i])
                break

    return composite_nums
