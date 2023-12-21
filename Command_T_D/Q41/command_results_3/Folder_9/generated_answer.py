import set
def identical_elements(a, b):
    if len(a) != len(b):
        return set()
    return set(a[70:200]) & set(b[70:200])
