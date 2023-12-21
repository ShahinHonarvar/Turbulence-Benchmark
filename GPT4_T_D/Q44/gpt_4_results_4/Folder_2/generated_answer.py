
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    comp_num = set()
    for i in range(35, min(len(lst),50)):
        if is_composite(lst[i]):
            comp_num.add(lst[i])
    return comp_num
