
def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]

    total_sum = sum(nums[a+1:b])

    missing_nums = [x for x in range(a+1, b) if x not in nums]

    if len(missing_nums) == 0:
        return ''

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
