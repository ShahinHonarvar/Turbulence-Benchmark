
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[12]
    missing = [num for num in range(a + 1, b) if num not in nums[10:13]]

    if not missing:
        return ''
        
    s = sum(missing)

    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]
