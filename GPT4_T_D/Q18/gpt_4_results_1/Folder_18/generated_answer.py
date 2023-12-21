
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for num in int_list[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            sum += num
    return sum
