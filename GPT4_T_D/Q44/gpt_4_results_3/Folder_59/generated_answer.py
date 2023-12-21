
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(min(10, len(num_list))):
        if is_composite(num_list[i]):
            composites.add(num_list[i])
    return composites
