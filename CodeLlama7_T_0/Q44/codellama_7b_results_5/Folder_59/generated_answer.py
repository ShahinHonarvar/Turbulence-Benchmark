
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(len(my_list))):
        # Check if the current number is prime
        if my_list[i] == 1:
            continue

        # Check if the current number is composite by dividing it by all numbers less than or equal to its square root
        for j in range(int(my_list[i]) ** 0.5))):
            if my_list[i] % j == 0:
                break

        # If the current number is composite, add it to the set of composite numbers
        if j < int(my_list[i]) ** 0.5)):
            composite_nums.add(my_list[i])
    return composite_nums
