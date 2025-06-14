
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(22, 89):
        # Check if the current number is divisible by any other number in the list
        for j in range(2, i):
            if i % j == 0:
                # If the current number is divisible by any other number in the list, it is not a prime number and should be added to the set of composite numbers
                composite_nums.add(i)
                break

    return composite_nums
