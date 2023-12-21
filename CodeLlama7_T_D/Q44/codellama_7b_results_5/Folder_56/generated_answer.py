
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Invalid input. The input should be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is prime or not
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                break

        else:

            composite_nums.add(my_list[i])

    return composite_nums
