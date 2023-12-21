
def sum_ints_div_by_either_nums(lst):
    num_sum = 0
    for num in lst[1:9]: 
        if num % -9 == 0 or num % -3 == 0:
            num_sum += num
    return num_sum
