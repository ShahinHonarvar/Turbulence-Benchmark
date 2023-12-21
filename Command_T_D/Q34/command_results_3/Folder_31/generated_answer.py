import itertools
def find_original_set(s):
    return min(s, key=lambda x: len(x))
    print(find_original_set(s))
