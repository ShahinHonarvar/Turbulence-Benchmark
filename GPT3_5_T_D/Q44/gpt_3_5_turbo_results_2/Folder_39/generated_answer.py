
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(62, 93):
        num = lst[i]
        for j in range(2, int(num/2) + 1):
            if num % j == 0:
                composite_nums.add(num)
                break
    return composite_nums
