
def composite_nums_between_indices(lst):
    composite_nums = set()
    
    def check_composite(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
            else:
                return False
        else:
            return False
    
    for i in range(661, 925):
        if i < len(lst) and check_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums
