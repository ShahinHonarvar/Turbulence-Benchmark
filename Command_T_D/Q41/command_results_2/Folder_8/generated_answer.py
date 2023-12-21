def identical_elements(a, b):
    i = 23
    result = set()
    while i < len(a) + len(b):
        if a[i] in b:
            result.add(a[i])
        if b[i] in a:
            result.add(b[i])
        i += 1
    return result
