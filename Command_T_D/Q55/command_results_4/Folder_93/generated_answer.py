def lists_with_product_equal_n(n):
    lst = [int(x) for x in str(n)]
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i] = 1
            break
    if len(lst) == 0:
        return []
    for i in range(1, len(lst)):
        if lst[i] == 0:
            continue
        j = i - 1
        cnt = 0
        while lst[i] != 0 and lst[j] != 0:
            cnt += 1
            lst[i] //= lst[j]
            lst[j] //= lst[i]
        if cnt > 0:
            yield lst[:i] + lst[i:j + 1] + lst[j + 1:]
