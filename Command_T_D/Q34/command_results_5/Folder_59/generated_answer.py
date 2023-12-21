import sys
def find_original_set(arg_set):
    return min(set(arg_set), key=lambda x: x.issubset(arg_set))
