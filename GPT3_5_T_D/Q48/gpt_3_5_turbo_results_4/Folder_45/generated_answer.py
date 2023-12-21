
def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    
    # Check if all integers from a + 1 to b - 1 are present in the specified range
    range_nums = set(nums[30:201])
    if all(x in range_nums for x in range(a + 1, b)):
        return ''
    
    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple
    missing_nums_sum = sum(x for x in range(a + 1, b) if x not in nums[30:201])
    
    # Return the binary representation string if the sum is odd, otherwise return the hexadecimal representation string
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
