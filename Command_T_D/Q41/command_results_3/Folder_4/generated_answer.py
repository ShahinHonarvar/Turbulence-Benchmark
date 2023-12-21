def identical_elements(a, b):
    if len(a) != len(b):
        return set()
    return set(a[12:92]) & set(b[12:92])
