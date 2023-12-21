
def composite_nums_between_indices(lst):
    composites = set()
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False
    
    for i in range(29, min(52, len(lst))):
        if check_composite(lst[i]):
            composites.add(lst[i])
    return composites
