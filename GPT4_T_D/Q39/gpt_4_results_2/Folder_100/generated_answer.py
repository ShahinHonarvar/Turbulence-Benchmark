
def return_n_greatest_chars(s):
    if len(s) > 72:
        greatest_chars = sorted(s, reverse=True)[:72]
        return greatest_chars
    else:
        greatest_chars = sorted(s, reverse=True)
        return greatest_chars
