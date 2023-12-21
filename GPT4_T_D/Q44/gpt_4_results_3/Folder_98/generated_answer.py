
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composites = set()
    for num in lst[0:7]:
        if is_composite(num):
            composites.add(num)
    return composites
