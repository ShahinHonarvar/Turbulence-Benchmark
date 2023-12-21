
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the divisible integers
    total = 0
    div_ints = []

    # Iterate through the list of integers and check if each integer is divisible by either 2 or 1 from index 0 to index 1, both inclusive
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0 or my_list[i] % 1 == 0:
            div_ints.append(my_list[i])
            total += div_ints[-1]

    # If no such integers exist in the specified range, return 0
    if not div_ints:
        return 0

    # Otherwise, return the sum of all divisible integers
    else:
        return total
