import heapq
def find_original_set(s):
    h = [(s, s)]
    hq = []
    while h:
        s, t = heapq.heappop(h)
        if t:
            hq.append(t)
        for i in s:
            t += {i}
            heapq.heappush(h, (t, t))
    return min(hq)
