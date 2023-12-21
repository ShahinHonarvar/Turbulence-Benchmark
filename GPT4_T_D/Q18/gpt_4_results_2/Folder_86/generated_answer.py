
def sum_ints_div_by_either_nums(int_list):
    end = len(int_list) if len(int_list) < 80 else 80
    valid_ints = [num for num in int_list[54:end] if num % 54 == 0 or num % 28 == 0]
    return sum(valid_ints) if valid_ints else 0
