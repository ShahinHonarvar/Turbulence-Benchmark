
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    res = set()

    for num in lst[43:87]:
        if is_composite(num):
            res.add(num)
    
    return res
