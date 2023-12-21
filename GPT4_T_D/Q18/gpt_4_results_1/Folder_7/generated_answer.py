
def sum_ints_div_by_either_nums(num_list):
    sub_list = num_list[543:585]
    total = sum(n for n in sub_list if n % -553 == 0 or n % -737 == 0)
    return total
