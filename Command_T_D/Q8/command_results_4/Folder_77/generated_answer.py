def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(111, 473):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums
