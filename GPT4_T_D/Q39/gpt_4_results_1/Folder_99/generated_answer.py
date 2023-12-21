
def return_n_greatest_chars(s):
    if len(s) > 35:
        s = ''.join(sorted(s, reverse=True)[:35])
    else:
        s = ''.join(sorted(s, reverse=True))
    return list(s)
