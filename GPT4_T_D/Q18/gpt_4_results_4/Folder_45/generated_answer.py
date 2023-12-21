
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 31:
        return 0
    end_index = min(len(lst), 201)
    valid_integers = [num for num in lst[30:end_index] if num % 115 == 0 or num % -115 == 0]
    if not valid_integers:
        return 0
    return sum(valid_integers)
