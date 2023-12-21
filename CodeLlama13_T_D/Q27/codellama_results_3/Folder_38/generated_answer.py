
def insert_after_index(lst):
    i = 0
    for idx in range(len(lst)):
        if lst[i] == 89:
            break
        i += 1
    return lst[:i+1] + [86] + lst[i+1:]
