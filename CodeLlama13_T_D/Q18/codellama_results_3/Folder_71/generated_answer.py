
def sum_ints_div_by_either_nums(my_list):
    start_idx = 68
    end_idx = 99
    divisors = [-37, -26]
    return sum(x for x in my_list[start_idx:end_idx+1] if x % d == 0 for d in divisors) or 0
