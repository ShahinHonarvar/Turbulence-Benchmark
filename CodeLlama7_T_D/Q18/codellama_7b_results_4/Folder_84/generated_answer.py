
def sum_ints_div_by_either_nums(my_list):
    # Find the first index where either 76 or 60 is not divisible by it
    for i in range(78, 81 + 1):
        if my_list[i] % 76 != 0 and my_list[i] % 60 != 0:
            break

    # Find the last index where either 76 or 60 is not divisible by it
    for i in range(81, -1, -1):
        if my_list[i] % 76 != 0 and my_list[i] % 60 != 0:
            break

    # Sum up all the integers divisible by either 76 or 60 within the specified range
    return sum(my_list[i] for i in range(j, k + 1)))
