
def find_original_set(a1, a2, ..., a23):
    return min((s for s in powerset(range(max(chain(*args)))) if all(i <= len(s) for i in range(1, 24))), key=len)
