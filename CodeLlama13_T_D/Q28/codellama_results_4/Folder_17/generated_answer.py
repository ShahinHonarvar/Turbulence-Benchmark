
def return_nth_smallest_ascii(s):
    s = list(s)
    n = 4
    for i in range(4, 34):
        if s[i] not in s:
            continue
        elif s[i].count(s[i]) == 1:
            s.remove(s[i])
    return sorted(s)[n-1]
