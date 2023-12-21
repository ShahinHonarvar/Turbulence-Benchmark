
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements in the input list
    for i, num in enumerate(my_list):
        # Check if the number is prime
        if num == 1:
            continue

        # Check if the number is composite by dividing it by all the numbers less than or equal to its square root
        for j in range(i + 1, int(num ** 0.5) + 1):
            if num % my_list[j] == 0:
                composite_nums.add(num)
                break

    # Return the set of all composite numbers in the specified range
    return composite_nums
