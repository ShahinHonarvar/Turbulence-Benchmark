
def sum_ints_div_by_either_nums(integers):
    return sum(num for num in integers[281:695] if num % -722 == 0 or num % -731 == 0) or 0
