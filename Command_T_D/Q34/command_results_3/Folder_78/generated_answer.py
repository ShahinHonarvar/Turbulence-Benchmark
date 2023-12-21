def find_original_set(arg_set):
    return min(set(range(1, 10 ** 9 + 7)), key=lambda x: x.issubset(arg_set))
