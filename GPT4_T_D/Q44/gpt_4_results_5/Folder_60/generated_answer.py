
def composite_nums_between_indices(l):
    composite_nums = set()
    for i in range(29, min(52, len(l))):
        count = 0
        for num in range(2, (l[i]//2)+1):
            if l[i] % num == 0:
                count += 1
        if count > 0:
            composite_nums.add(l[i])
    return composite_nums
