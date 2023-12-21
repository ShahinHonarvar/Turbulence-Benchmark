
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of the input list
    for i in range(26, 75):

        # Check if the current element is divisible by 80
        if my_list[i] % 80 == 0:

            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by 80 from index 26 to index 74, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return div_ints
