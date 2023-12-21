
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return True
        return False
    
    composite_nums = set()
    for index in range(639, 976):
        if is_composite(lst[index]):
            composite_nums.add(lst[index])
    
    return composite_nums
