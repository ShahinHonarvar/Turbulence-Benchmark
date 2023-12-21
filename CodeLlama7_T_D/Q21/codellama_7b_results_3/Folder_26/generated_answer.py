
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    div_list = []

    # Loop through the list and check if each integer is divisible by 39

    for i in range(45, 81):
        if my_list[i] % 39 == 0:
            div_list.append(my_list[i])

    # Return the list of all integers divisible by 39 from index 45 to index 80, both inclusive. If no such integers exist in the specified range, the function should return an empty list.

    return div_list
