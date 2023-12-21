
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list and check if each integer is divisible by 99
    for i in range(len(my_list)):
        if my_list[i] % 99 == 0:
            # If the integer is divisible by 99, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by 99 from index 62 to index 63, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return div_ints
