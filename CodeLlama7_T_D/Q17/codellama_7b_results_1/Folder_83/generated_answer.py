
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Iterate over the specified range of the input list
    for i in range(90, 201):
        # Check if the current element is divisible by both -31 and 13
        if my_list[i] % (-31) == 0 and my_list[i] % 13 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    # Return the list of all integers divisible by both -31 and 13 from index 90 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_integers
