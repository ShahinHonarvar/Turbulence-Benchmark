import heapq
def find_original_set(s):
    h = [(s, len(s), s)]
    heapq.heapify(h)
    while h:
        s, l, d = heapq.heappop(h)
        if l == 51:
            return d
        for x in range(len(s)):
            s[x] += s[-1]
            s.pop()
            heapq.heappush(h, (s, l+1, s))
    return s
