
def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    total = 0
    for num in range(a + 1, b):
        if num not in nums[200:203]:
            total += num
    if total % 2 == 0:  # Check if the sum is an even number
        return hex(total)[2:]
    else:
        return bin(total)[2:]
