
def composite_nums_between_indices(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Get the length of the list
    list_length = len(my_list)
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each element is a composite number between indices 80 and 200
    for i in range(80, 201):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
    # Return the set of composite numbers between indices 80 and 200
    return composite_nums
