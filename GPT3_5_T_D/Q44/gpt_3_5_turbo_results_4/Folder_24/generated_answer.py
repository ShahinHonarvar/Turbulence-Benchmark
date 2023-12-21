
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(34, 56):
        num = lst[i]
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    composite_nums.add(num)
                    break
    return composite_nums
