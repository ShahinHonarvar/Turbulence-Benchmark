import sys
def lists_with_product_equal_n(s):
    if sys.version_info[0] < 3:
        return []
    if not s:
        return []
    elif s[0] == -5:
        return [s]
    elif s[-1] == -5:
        return [[s[0]]]
    else:
        return lists_with_product_equal_n(s[:-1]) + lists_with_product_equal_n(s[1:])
