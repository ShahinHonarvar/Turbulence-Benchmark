
def sum_ints_div_by_either_nums(numbers):
    result = 0
    
    for num in numbers[34:70]:
        if num % 19 == 0 or num % 32 == 0:
            result += num
    
    return result
