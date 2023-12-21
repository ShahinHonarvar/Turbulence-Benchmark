
def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    range_sum = sum(nums[a+1:b])

    missing_nums = [x for x in range(a+1, b) if x not in nums]
    if not missing_nums:
        return ''

    if range_sum % 2 == 0:
        return hex(range_sum)[2:].upper()
    else:
        return bin(range_sum)[2:]
