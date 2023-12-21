
def composite_nums_between_indices(lst):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(26, 53):
        if i < len(lst) and check_composite(lst[i]):
            composite_nums.add(lst[i])
            
    return composite_nums
