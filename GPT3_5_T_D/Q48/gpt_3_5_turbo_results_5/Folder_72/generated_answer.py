
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    
    missing_nums = [x for x in range(a+1, b) if x not in numbers[13:71]]
    
    if len(missing_nums) == 0:
        return ''
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
