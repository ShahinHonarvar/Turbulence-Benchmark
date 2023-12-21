import itertools
def lists_with_product_equal_n(s):
    for i in range(1, len(s)):
        for j in range(i, len(s)):
            for k in range(j, len(s)):
                p = s[i:j] + s[j:k] + s[k:]
                if len(p) > 0 and p[0] * p[-1] == 93:
                    yield p
    for p in itertools.permutations(s, 2):
        if p[0] * p[1] == 93:
            yield p
