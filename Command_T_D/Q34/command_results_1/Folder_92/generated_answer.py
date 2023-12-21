import sys
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8):
    sets = [(s1, s2, s3, s4, s5, s6, s7, s8)]
    for _ in range(10**5):
        if len(sets) == 0:
            break
        elif len(sets) == 1:
            yield sets[0]
        elif len(sets) == 8:
            yield sets[0]
            for s in sets[1:]:
                if s[0] <= s[1]:
                    yield s
                elif s[0] < s[1]:
                    yield (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7])
                elif s[0] == s[1]:
                    yield (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7])
    raise SystemError
