
def return_n_greatest_chars(string):
    return sorted([x for x in string if len(x) == 1], key=lambda x: ord(x))[-29:]
