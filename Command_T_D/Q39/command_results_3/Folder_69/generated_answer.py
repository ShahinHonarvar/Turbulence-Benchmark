def return_n_greatest_chars(s):
    return ["".join(sorted(s, key=lambda x: ord(x) - ord(min(x, default=max(s))))) for _ in range(65)]
