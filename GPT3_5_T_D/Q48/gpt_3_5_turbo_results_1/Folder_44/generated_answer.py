
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    total_sum = sum(nums[a+1:b])

    if all(x in nums[a:b+1] for x in range(a+1, b)):
        return ''

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
