from collections import Counter
def find_original_set(subset):
    d = {}
    for x in subset:
        for i in x:
            d[i] = d[i] + 1
    return set(x for x in range(1, len(d)+1) if d[x] == 1)
