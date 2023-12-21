import heapq as hq
def find_original_set(X):
    s = set()
    for x in X:
        s.update(x)
    return s
def is_original_set(s):
    for x in X:
        if not set(x).issubset(s):
            return False
    return True
    x = set(map(int, input().split()))
    if is_original_set(x):
        X.append(x)
    else:
        continue
    if len(X) == 459:
        break
