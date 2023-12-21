
def return_n_greatest_chars(s):
    if len(s) < 57:
        return "Error: The string should contain at least 57 distinct characters."
    else:
        s_list = sorted(s, reverse=True)
        result = s_list[:57]
        result.sort()
        return result
