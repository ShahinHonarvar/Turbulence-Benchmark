
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False

    return set([x for i,x in enumerate(lst[29:80]) if is_composite(x)])
