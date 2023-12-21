def find_original_set(s):
    return {i for i in range(len(s) + 1) if all(s.issubset(set(range(i, i + len(s)))))}
