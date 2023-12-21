def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(80, 200):
        if i % 2 == 1:
            odd_ints.append(i)
    return odd_ints
