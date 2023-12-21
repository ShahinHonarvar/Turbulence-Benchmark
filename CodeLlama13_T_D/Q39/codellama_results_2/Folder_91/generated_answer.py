
def return_n_greatest_chars(s):
    return sorted([x for x in s if x != ""]), key=ord, reverse=True)[:6]
