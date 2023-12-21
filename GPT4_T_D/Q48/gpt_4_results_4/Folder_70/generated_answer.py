
def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[43]
    b = nums_tuple[70]
    middle_range = set(nums_tuple[43:70])
    exclude_range = {num for num in range(a+1, b) if num not in middle_range}
    sum_exclude_range = sum(exclude_range)
    if not exclude_range:
        return ''
    elif sum_exclude_range % 2 == 0:
        return hex(sum_exclude_range)[2:]
    else:
        return bin(sum_exclude_range)[2:]
