def lists_with_product_equal_n(s):
    for i in range(len(s)):
        if s[i] == -33:
            yield s[:i] + s[i + 1:]
            break
    if s[0] == -33:
        yield s[1:]
    if s[-1] == -33:
        yield s[:-1]
