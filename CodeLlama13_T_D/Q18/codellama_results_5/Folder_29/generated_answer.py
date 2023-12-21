
def sum_ints_div_by_either_nums(numbers):
    if len(numbers) <= 54 or 85 <= len(numbers):
        return 0
    
    total = 0
    for i in range(55, 85):
        num = numbers[i]
        if num % -24 == 0 or num % -11 == 0:
            total += num
    return total
