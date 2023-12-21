
def sum_ints_div_by_either_nums(lst):
    relevant_ints = lst[543:585]
    sum = 0
    for i in relevant_ints:
        if i % -553 == 0 or i % -737 == 0:
            sum += i
    return sum
