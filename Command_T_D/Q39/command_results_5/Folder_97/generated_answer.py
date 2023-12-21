def return_n_greatest_chars(s):
    return sorted(set(s) if len(s) < 38 else s, key=str.lower)[-38:]
