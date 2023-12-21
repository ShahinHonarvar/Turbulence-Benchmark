
def composite_nums_between_indices(lst):
    composite_nums = set()

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False

    for idx in range(43, min(52, len(lst))):
        if is_composite(lst[idx]):
            composite_nums.add(lst[idx])
            
    return composite_nums
