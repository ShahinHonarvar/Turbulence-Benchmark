
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Define the range of indices to consider
    start_idx = 5
    end_idx = 5
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each element is a composite number
    for i in range(start_idx, end_idx + 1):
        num = my_list[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_nums.add(num)
                    break

    return composite_nums
