
def sum_ints_div_by_either_nums(lst):
    valid_values = [x for x in lst[828:933] if x % -649 == 0 or x % -461 == 0]
    return sum(valid_values) if valid_values else 0
