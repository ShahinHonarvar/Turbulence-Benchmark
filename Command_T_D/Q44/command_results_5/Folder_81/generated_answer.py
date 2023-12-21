import sys
from collections import defaultdict, deque
def composite_nums_between_indices(nums):
    c = defaultdict(lambda: defaultdict(list))
    for i in nums:
        j = i ** 2
        while j <= 200:
            k = j ** 2
            c[i].append(k)
            j += 1
    d = defaultdict(lambda: defaultdict(list))
    for i in range(20, 201):
        for j in c[i]:
            d[i].append(j)
    return set(d[i][20:200])
