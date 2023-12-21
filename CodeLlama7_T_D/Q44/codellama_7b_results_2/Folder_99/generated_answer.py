
def composite_nums_between_indices(my_list):
    # Check if the input argument is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input argument must be a list of positive integers.")
    # Define a set to store the composite numbers between indices 246 and 750
    composite_nums = set()
    # Iterate over the elements of the input list
    for i in range(len(my_list)):
        # Check if the current element is greater than or equal to 246 and less than or equal to 750
        if my_list[i] >= 246 and my_list[i] <= 750:
            # Check if the current element is composite by dividing it by all prime numbers less than or equal to its square root
            for p in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % p == 0:
                    # If the current element is composite, add it to the set of composite numbers between indices 246 and 750
                    composite_nums.add(my_list[i])
    return composite_nums
