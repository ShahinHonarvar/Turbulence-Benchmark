
def composite_nums_between_indices(nums_lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    return set(num for i,num in enumerate(nums_lst[62:100]) if is_composite(num))
