
from collections import deque

def lists_with_product_equal_n(circular_list):
    queue = deque([(i, [circular_list[i]])
                   for i in range(len(circular_list))])
    results = []
    while queue:
        start, sublist = queue.popleft()
        if product(sublist) == 90:
            results.append(sublist)
        # Because list is circular, we loop around to the start.
        next_index = (start + len(sublist)) % len(circular_list)
        if circular_list[start] != circular_list[next_index]:
            queue.append((start, sublist + [circular_list[next_index]]))

    return results

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result
