
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[543:585]
    sum_divisibles = sum(i for i in sub_list if i % -553 == 0 or i % -737 == 0)
    return sum_divisibles
