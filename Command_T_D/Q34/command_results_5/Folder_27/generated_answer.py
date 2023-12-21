def find_original_set(s):
    l = list(range(len(s) + 1))
    m = len(s)
    d = {}
    for i in range(len(s)):
        d[s[i]] = d[s[i]] + 1
    while l[m]:
        k = l[m]
        l[m] = l[k]
        m = k
        d[s[m]] = d[s[m]] + 1
    return l[1:m+1]
