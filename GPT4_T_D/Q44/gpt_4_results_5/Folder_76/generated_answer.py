
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False
    
    result_set = set()
    for i in range(639, min(976, len(lst))):
        if is_composite(lst[i]):
            result_set.add(lst[i])
    return result_set
