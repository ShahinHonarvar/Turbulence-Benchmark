
def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in num_list[240:902]:
        if i % 546 == 0 or i % 709 == 0:
            sum += i
    return sum
