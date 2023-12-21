def find_original_set(s):
    return {i for i in range(len(s) + 1) if all(i in j for j in s)}
