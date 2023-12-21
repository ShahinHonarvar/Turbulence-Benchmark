import itertools
def lists_with_product_equal_n(s):
    return [s[i:j] for i in range(len(s)) for j in range(i, len(s)) if -9 == s[i:j].prod()]
