
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers starting from index 13 to index 76, both inclusive
    for i in range(13, 77):
        # Check if the current integer is divisible by both -66 and -32
        if my_list[i] % (-66) == 0 and my_list[i] % (-32) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -66 and -32 from index 13 to index 76, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
