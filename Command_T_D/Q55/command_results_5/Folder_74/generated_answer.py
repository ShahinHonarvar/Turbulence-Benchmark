def lists_with_product_equal_n(s):
    return [s[i:i + m] for i in range(len(s) - 1) for m in range(1, len(s) - i + 1) if len(s[i:i + m]) > 1 and s[i:i + m][-1] == 51]
