
def composite_nums_between_indices(lst):
    def is_composite(n):
        for i in range(2, n):
            if n%i == 0: 
                return True
        return False

    composite_nums = set()
    for i in range(55, 99):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])

    return composite_nums
