import heapq as hq
def find_original_set(s):
    s = set(s)
    hq.heapify(s)
    m = set()
    while s:
        x = hq.heappop(s)
        if not m & x:
            m.add(x)
            for i in s:
                if m & i:
                    break
            else:
                hq.heappush(s,x)
                break
    return m
