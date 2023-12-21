
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i, num in enumerate(my_list):
        # Check if the number is between index 28 to index 38, both inclusive
        if 28 <= i <= 38:
            # Use the math.floor() function to find the greatest integer less than or equal to the number
            floor_num = math.floor(num)
            # Check if the number is composite by dividing it by all numbers from 2 to the square root of the number
            for j in range(2, int(math.sqrt(floor_num))) + 1:
                if floor_num % j == 0:
                    # If the number is composite, add it to the set
                    composite_nums.add(num)
                    # Break out of the inner loop since we have found a factor
                    break

    # Return the set of all composite numbers in the given list that are between index 28 to index 38, both inclusive
    return composite_nums
