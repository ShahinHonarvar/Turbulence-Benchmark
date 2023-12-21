
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    result = set()
    for i in range(91, min(100, len(lst))):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result
