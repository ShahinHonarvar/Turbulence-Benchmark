
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(len(my_list))):
        # Check if the current number is a prime number
        if my_list[i] == 1 or any(my_list[i] % x == 0 for x in range(2, int(my_list[i]) ** 0.5 + 1)))):
            continue

        # If the current number is not a prime number, add it to the set of composite numbers
        else:
            composite_nums.add(my_list[i])
    # Return the set of composite numbers between indices 43 and 51 (inclusive)
    return composite_nums
