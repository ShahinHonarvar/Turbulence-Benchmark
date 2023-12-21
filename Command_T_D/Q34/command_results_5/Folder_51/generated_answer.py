import heapq as hq
def find_original_set(sets):
    seen = set()
    for s in sets:
        for e in s:
            seen.add(e)
    return seen
def find_original_set(sets):
    hq.heapify(sets)
    seen = set()
    for s in sets:
        for e in s:
            seen.add(e)
    return seen
