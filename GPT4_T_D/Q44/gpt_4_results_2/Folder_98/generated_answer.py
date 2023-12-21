
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return True
        return False

    comps = set()
    for i in range(min(7, len(num_list))):
        if is_composite(num_list[i]):
            comps.add(num_list[i])
    return comps
