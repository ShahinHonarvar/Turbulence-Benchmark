def find_original_set(S):
    import heapq
    import collections
    s = set(S)
    s = list(s)
    s.sort()
    heapq.heapify(s)
    cur = collections.defaultdict(list)
    for x in s:
        cur[x].append(x)
    m = len(s)
    return s[:m]
