
def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    total_sum = sum(nums[a+1:b])
    missing_nums = [x for x in range(a+1, b) if x not in nums]
    
    if missing_nums == []:
        return ''
    else:
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
