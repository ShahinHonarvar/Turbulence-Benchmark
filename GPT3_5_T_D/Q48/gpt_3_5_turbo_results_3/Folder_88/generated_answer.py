
def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    
    missing_nums = []
    for i in range(a+1, b):
        if i not in nums[3:9]:
            missing_nums.append(i)
    
    if len(missing_nums) == 0:
        return ""
    
    sum = 0
    for num in missing_nums:
        sum += num
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
