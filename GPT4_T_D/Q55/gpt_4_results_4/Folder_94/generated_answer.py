
def lists_with_product_equal_n(lst):
    n = -30
    size = len(lst)
    result = []
    for start in range(size):
        for end in range(start+1, size+1):
            sublist = lst[start:end]
            plist = 1
            for num in sublist:
                plist *= num
            if plist == n:
                result.append(sublist)
        for end in range(0, start):
            sublist = lst[start:] + lst[:end]
            plist = 1
            for num in sublist:
                plist *= num
            if plist == n:
                result.append(sublist)
    return result
