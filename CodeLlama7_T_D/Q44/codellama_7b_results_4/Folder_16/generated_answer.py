
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list and check if each number is composite
    for i, num in enumerate(my_list):
        # Check if the current number is between index 40 and 80 (inclusive)
        if 40 <= i <= 80:
            # Check if the current number is composite by dividing it by all numbers less than or equal to its square root
            for j in range(1, int(num ** 0.5) + 1):
                if num % j == 0:
                    # If the current number is composite, add it to the set of composite numbers
                    composite_nums.add(num)
                    # Break out of the inner loop since we have found a divisor
                    break
    return composite_nums
