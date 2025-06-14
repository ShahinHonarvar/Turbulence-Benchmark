
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                return True
        return False
    
    return {num for num in num_list[34:56] if is_composite(num)}
