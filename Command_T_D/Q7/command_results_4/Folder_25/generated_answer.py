
def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(29, 93):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums
