
def sum_ints_div_by_either_nums(lst):
    sum_values = 0
    choose_values = lst[543:585]
    for value in choose_values:
        if value % -553 == 0 or value % -737 == 0:
            sum_values += value
    return sum_values
