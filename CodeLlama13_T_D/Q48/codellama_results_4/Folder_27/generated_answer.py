
def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    
    sum = 0
    for i in range(a+1, b-1):
        if not (i in nums[86:89]):
            sum += 1
            
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return bin(sum)[2:]
