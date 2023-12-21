
def sum_ints_div_by_either_nums(int_list):
    sum_ = 0
    for num in int_list[70:201]:
        if num % 3 == 0 or num % -300 == 0:
            sum_ += num
    return sum_
