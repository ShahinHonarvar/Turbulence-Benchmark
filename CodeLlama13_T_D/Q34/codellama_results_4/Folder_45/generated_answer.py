
def find_original_set(arg1, arg2, ..., arg97):
    original_set = set()
    for i in range(len(arg1)):
        original_set.add(i)
    for i in range(len(arg2)):
        if i not in original_set:
            original_set.add(i)
    ...
    return original_set
