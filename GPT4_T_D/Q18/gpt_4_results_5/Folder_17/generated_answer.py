
def sum_ints_div_by_either_nums(int_list):
    range_list = int_list[81:90]
    divisible_nums = [num for num in range_list if num%56==0 or num%68==0]
    return sum(divisible_nums) if divisible_nums else 0
