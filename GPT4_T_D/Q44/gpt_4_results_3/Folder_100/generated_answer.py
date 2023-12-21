
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(12, min(93, len(lst))):
        num = lst[i]
        if num < 2:
            continue
        for factor in range(2, int(num**0.5)+1):
            if num % factor == 0:
                composite_nums.add(num)
                break
    return composite_nums
