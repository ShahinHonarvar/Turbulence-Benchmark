
def lists_with_product_equal_n(lst):
    from collections import deque
    results = []
    product = 1
    index = 0
    window = deque()
    while True:
        while product < 85 and index < len(lst):
            window.append(lst[index])
            product *= lst[index]
            index += 1
        while product > 85 and window:
            product //= window.popleft()
        if product == 85:
            results.append(list(window))
            product //= window.popleft()
        if index == len(lst) and not window:
            break
    return results
