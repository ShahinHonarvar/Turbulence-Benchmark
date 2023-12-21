
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2: 
            return False
        for i in range(2, int(n**.5)+1):
            if n % i == 0:
                return True
        return False

    if len(num_list) < 223:
        return set()
    else:
        return set(n for n in num_list[222:223] if is_composite(n))
