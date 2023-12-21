
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    
    missing_nums = [i for i in range(a+1, b) if i not in nums]
    if len(missing_nums) == 0:
        return ""
    
    sum = 0
    for num in missing_nums:
        sum += num
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
