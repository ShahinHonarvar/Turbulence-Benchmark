
def sum_ints_div_by_either_nums(lst):
    start_index = max(81, 0)
    end_index = min(86, len(lst)-1)
    sub_list = lst[start_index:end_index+1]
    sum = 0
    for i in sub_list:
        if i % -33 == 0 or i % -62 == 0:
            sum += i
    return sum
