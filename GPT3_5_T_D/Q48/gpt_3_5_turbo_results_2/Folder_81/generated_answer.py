
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]

    total = 0
    for num in range(a + 1, b):
        if num not in nums[10:101]:
            total += num

    if total % 2 == 0:  # Even
        return hex(total)[2:]
    else:  # Odd
        return bin(total)[2:]
