import itertools
def lists_with_product_equal_n(int_list):
    return [sub for sub in itertools.permutations(int_list) if all(a == b == c == 1 for a, b, c in zip(sub, sub[1:], sub[2:] + [sub[0]])) and len(sub) == 3]
