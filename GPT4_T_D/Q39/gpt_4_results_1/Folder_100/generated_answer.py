
def return_n_greatest_chars(string):
    if len(string) > 72:
        n_greatest_chars = sorted(string, reverse=True)[:72]
        return n_greatest_chars
    else:
        return "String contains less than 72 characters"
