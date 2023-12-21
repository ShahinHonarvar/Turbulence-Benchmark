import heapq
def find_original_set(arg):
    result = set()
    for i in range(len(arg)):
        result.update(arg[i])
    heapq.heapify(result)
    return heapq.heappop(result)
