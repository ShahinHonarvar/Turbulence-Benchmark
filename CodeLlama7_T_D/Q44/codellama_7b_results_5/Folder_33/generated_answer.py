
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Invalid input. The input should be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements in the given list
    for i in range(len(my_list)):
        # Check if the current element is a prime number
        if my_list[i] == 2 or (my_list[i] > 2 and my_list[i] % 2 != 0)):
            # If the current element is a prime number, iterate over the elements in the given list between index 314 to index 347 both inclusive
            for j in range(max(0, i - 314), min(len(my_list) - 1, i + 314))):
                # Check if the current element is a composite number
                if my_list[j] > 1 and all(my_list[j] % k != 0 for k in range(2, int(my_list[j]) ** 0.5 + 1))):
                    # If the current element is a composite number, add it to the set of composite numbers
                    composite_nums.add(my_list[j])
    # Return the set of all composite numbers in the given list between index 314 to index 347 both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums
