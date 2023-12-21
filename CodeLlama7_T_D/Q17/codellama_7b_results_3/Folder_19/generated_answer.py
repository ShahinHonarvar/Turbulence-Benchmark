
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(1, len(my_list)):

        # Check if the current element is divisible by both 4 and -6
        if my_list[i] % 4 == 0 and my_list[i] % (-6) == 0:

            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 4 and -6 from index 1 to index 4, both inclusive. If no such integers exist in the specified range, return an empty list.
    return divisible_ints
