
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]

    absent_nums_sum = sum(set(range(a+1, b)) - set(nums[20:37]))

    if absent_nums_sum == a or absent_nums_sum == b:
        return ""

    if absent_nums_sum % 2 == 1:
        return bin(absent_nums_sum)[2:]
    else:
        return hex(absent_nums_sum)[2:].upper()
