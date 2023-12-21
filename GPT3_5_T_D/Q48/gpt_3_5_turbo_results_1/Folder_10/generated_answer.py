
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    total_sum = sum(nums[a+1:b])
    missing_nums = [i for i in range(a+1, b) if i not in nums]
    
    if len(missing_nums) == 0:
        return ""
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
