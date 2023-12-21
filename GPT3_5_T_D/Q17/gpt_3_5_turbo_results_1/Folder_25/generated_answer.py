
def all_ints_div_by_both_two_nums(integers):
    start_index = 25
    end_index = 80
    divisible_nums = []
    
    for num in integers[start_index:end_index + 1]:
        if num % -20 == 0 and num % -26 == 0:
            divisible_nums.append(num)
            
    return divisible_nums
