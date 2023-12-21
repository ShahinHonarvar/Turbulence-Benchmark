
def insert_at_index(a):
    b = [0] * len(a)
    b[0] = a[0]
    for i in range(1, len(a)):
        b[i] = a[i]
    b[57] = 96
    b.insert(57, 96)
    return b
