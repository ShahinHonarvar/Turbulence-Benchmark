
def sum_ints_div_by_either_nums(my_list):
    # Find the index of the first element that is divisible by either 39 or 15
    first_divisible_index = None
    for i in range(44, 60):
        if my_list[i] % 39 == 0 or my_list[i] % 15 == 0:
            first_divisible_index = i
            break

    # If no elements are divisible by either 39 or 15, return 0
    if first_divisible_index is None:
        return 0

    # Sum up all the integers from the first divisible index to the end of the list, inclusive
    sum = 0

    for i in range(first_divisible_index, len(my_list)):
        sum += my_list[i]

    return sum
