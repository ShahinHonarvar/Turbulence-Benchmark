
def composite_nums_between_indices(lst):
    def is_composite(num):
        factors = [i for i in range(1,num+1) if num % i == 0]
        return len(factors) > 2
    
    return {num for num in lst[28:33] if is_composite(num)}
