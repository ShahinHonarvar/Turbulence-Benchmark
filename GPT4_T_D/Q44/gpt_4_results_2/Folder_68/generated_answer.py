
def composite_nums_between_indices(lst):
    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return True
        return False

    return {element for index, element in enumerate(lst[:9]) if is_composite(element)}
