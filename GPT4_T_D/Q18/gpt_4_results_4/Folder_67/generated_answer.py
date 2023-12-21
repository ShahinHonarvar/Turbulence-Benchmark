
def sum_ints_div_by_either_nums(integer_list):
    sublist = integer_list[24:33]
    sum = 0
    for num in sublist:
        if num % 35 == 0 or num % 87 == 0:
            sum += num
    return sum
