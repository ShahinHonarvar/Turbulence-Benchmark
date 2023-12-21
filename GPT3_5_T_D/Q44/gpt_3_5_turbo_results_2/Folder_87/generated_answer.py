
def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[43:52]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    composite_nums.add(num)
                    break
    return composite_nums
