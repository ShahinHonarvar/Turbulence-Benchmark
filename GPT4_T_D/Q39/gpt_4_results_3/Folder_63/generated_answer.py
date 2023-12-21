
def return_n_greatest_chars(chars):
    if len(set(chars)) >= 44:    
        char_list = sorted([char for char in set(chars)], key=ord, reverse=True)[:44]
        return sorted(char_list)
    else:
        return "The input string must have at least 44 distinct characters."
