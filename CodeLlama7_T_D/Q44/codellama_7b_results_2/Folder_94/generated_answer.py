
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Define the range of indices to consider
    start_index = 27
    end_index = 55
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check for each number if it is prime or not
    for i in range(start_index, end_index + 1):
        num = my_list[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                composite_nums.add(num)
    # Return the set of all composite numbers in the given list that are between index 27 to index 55, both inclusive
    return composite_nums
