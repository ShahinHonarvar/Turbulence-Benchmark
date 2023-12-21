def return_n_greatest_chars(s):
    return sorted(s, key=str.encode)[-44:]
