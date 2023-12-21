
def sum_ints_div_by_either_nums(int_list):
    numbers = int_list[:2]
    sum_of_nums = sum(num for num in numbers if num % 4 == 0 or num % -6 == 0)
    return sum_of_nums
