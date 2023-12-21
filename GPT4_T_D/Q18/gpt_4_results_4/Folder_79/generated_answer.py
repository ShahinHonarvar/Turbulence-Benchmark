
def sum_ints_div_by_either_nums(ints):
    valid_nums = [num for num in ints[8:10] if num%6==0 or num%(-3)==0]
    return sum(valid_nums) if valid_nums else 0
