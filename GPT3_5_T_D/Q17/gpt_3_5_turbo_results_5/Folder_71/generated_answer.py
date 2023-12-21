 
def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for num in lst[68:100]:
        if num % -37 == 0 and num % -26 == 0:
            divisible_by_both.append(num)
            
    return divisible_by_both
