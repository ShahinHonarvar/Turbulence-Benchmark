
def return_n_greatest_chars(s):
    if len(set(s)) < 35:
        return "The string should contain at least 35 distinct characters"
    else:
        return sorted(list(set(s)), key=ord, reverse=True)[:35]
