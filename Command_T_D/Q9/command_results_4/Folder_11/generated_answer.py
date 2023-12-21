def all_odd_ints_inclusive(nums):
    output = []
    for i in range(37, 51):
        if i % 2 == 0:
            continue
        output.append(nums[i])
    return output
