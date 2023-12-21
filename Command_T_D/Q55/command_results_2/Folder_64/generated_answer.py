def lists_with_product_equal_n(s):
    for i in range(len(s)):
        if s[i] == 3:
            yield [3]
        elif s[i] == 1:
            yield [3, 3, 1]
        elif s[i] == 2:
            yield [3, 2, 2]
        else:
            continue
