
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    range_sum = sum(num for num in range(a+1, b) if num not in nums[1:7])
    
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()
