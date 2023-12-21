import sys
import heapq
def find_original_set(X):
    sets = [set(map(int, input_text().split())) for _ in range(80)]
    minset = set()
    for s in sets:
        if X & s == s:
            heapq.heappush(minset, s)
    return minset
