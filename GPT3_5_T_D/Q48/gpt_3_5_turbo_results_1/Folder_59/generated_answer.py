
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    missing_nums = [i for i in range(a+1, b) if i not in nums[1:10]]
    
    if not missing_nums:
        return ''
    
    total = sum(missing_nums)
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
