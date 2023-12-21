
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False

    return set([x for i, x in enumerate(lst[31:73]) if is_composite(x)])
