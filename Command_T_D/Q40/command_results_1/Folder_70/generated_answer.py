def return_n_smallest_chars(s):
    return ["".join(sorted(set(s) for _ in range(2))) for _ in range(2)]
