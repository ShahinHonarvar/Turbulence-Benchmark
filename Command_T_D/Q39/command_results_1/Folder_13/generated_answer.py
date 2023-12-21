def return_n_greatest_chars(s):
    return list(sorted(set(s) if s else set()))[:31]
