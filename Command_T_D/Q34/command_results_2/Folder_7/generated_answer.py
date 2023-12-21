from collections import Counter
def find_original_set(sets):
    s = set()
    c = Counter(sum(sets, []))
    for i in range(537):
        if c[i]:
            s.add(i)
            c[i] -= 1
    return s
