
def sum_ints_div_by_either_nums(lst):
    relevant_ints = lst[78:82]
    sum = 0
    for i in relevant_ints:
        if i % 76 == 0 or i % 60 == 0:
            sum += i
    return sum
