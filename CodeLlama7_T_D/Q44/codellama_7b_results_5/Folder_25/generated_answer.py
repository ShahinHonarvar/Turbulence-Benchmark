
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(75, 94+1):

        # Check if the current number is divisible by any of the numbers in the range [2, sqrt(i)]
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(i)

    # Return the set of all composite numbers between indices 75 and 94 (both inclusive), or an empty set if no such number exists.
    return composite_nums
