
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each element is a composite number
    for i in range(2, len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break
    # Return the set of all composite numbers in the specified range
    return composite_nums
