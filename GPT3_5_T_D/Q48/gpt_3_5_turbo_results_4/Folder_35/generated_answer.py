
def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in numbers[77:85]:
            missing_nums.append(num)
    
    if len(missing_nums) == 0:
        return ""
    
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
