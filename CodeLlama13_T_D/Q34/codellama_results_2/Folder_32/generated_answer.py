
def find_original_set(arg1, arg2, ..., arg459):
    original_set = set()
    for i in range(len(arg1)):
        if i not in original_set:
            original_set.add(i)
    for j in range(len(arg2)):
        if j not in original_set:
            original_set.add(j)
    ...
    for k in range(len(arg459)):
        if k not in original_set:
            original_set.add(k)
    return original_set
