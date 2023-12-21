
def all_ints_div_by_both_two_nums(my_list):
    # List of integers divisible by 32 and 44
    result = []

    # Iterate over the list from index 72 to index 93, both inclusive
    for i in range(72, 94):
        if my_list[i] % 32 == 0 and my_list[i] % 44 == 0:
            result.append(my_list[i])

    return result
