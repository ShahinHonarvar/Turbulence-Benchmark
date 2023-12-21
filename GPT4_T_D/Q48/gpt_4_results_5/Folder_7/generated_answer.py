
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]

    range_set = set(range(a + 1, b))
    tuple_set = set(nums[11:97])

    missing_nums_sum = sum(range_set - tuple_set)

    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
