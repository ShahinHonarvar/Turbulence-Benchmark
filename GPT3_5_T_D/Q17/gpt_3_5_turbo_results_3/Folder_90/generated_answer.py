
def all_ints_div_by_both_two_nums(integer_list):
    div_nums = [-863, -329]
    result = []
    
    for i in range(138, 425):
        if all(integer % div == 0 for div in div_nums for integer in integer_list[i]):
            result.append(integer_list[i])
    
    return result
