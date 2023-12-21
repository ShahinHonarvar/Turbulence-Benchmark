
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
   
    return {lst[i] for i in range(len(lst)) if i <= 0 and is_composite(lst[i])}
