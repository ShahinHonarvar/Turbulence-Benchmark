
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list
    for i in range(20, 201):

        # Check if the current element is divisible by 4
        if my_list[i] % 4 == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 4 from index 20 to index 200, both inclusive
    return divisible_ints
