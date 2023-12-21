
def composite_nums_between_indices(int_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composite_nums = {num for num in int_list[25:60] if is_composite(num)}
    
    return composite_nums
