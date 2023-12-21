
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    numbers_in_range = set(nums[11:100])
    
    total = 0
    for num in range(a+1, b):
        if num not in numbers_in_range:
            total += num
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
