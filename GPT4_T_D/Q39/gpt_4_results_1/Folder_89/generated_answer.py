
def return_n_greatest_chars(s):
    if len(s) < 55: 
        return "Input string should have at least 55 distinct characters"
    else:
        return sorted(sorted(s, key=ord)[-55:])
