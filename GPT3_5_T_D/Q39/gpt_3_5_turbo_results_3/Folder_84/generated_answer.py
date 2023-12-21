
def return_n_greatest_chars(s):
    if len(s) < 10:
        return sorted(list(s), reverse=True)
    else:
        return sorted(list(s), reverse=True)[:10]
