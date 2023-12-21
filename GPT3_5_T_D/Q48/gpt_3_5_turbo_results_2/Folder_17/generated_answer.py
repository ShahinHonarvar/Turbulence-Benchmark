
def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    
    # Check if all numbers from a + 1 to b - 1 are present in the range
    if all(i in nums[73:85] for i in range(a + 1, b)):
        return ""
    
    # Calculate the sum of numbers not present in the range
    total = sum(i for i in range(a + 1, b) if i not in nums[73:85])
    
    # Check if the sum is odd or even
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
