
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list
    for i in range(40, 201):
        # Check if the current integer is divisible by both 21 and 71
        if my_list[i] % 21 == 0 and my_list[i] % 71 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 21 and 71 from index 40 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
