
def sum_ints_div_by_either_nums(my_list):
    # Calculate the sum of all integers divisible by either 15 or 87 from index 42 to index 43, both inclusive
    sum = 0
    for i in range(42, 43 + 1):
        if my_list[i] % 15 == 0 or my_list[i] % 87 == 0:
            sum += my_list[i]
    return sum
