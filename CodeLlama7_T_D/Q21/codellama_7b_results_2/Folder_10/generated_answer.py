
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(42, 89 + 1):
        # Check if the current element is divisible by -59
        if my_list[i] % -59 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -59 from index 42 to index 89, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
