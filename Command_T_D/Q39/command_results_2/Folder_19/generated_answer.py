import string
def return_n_greatest_chars(str_arg):
    result = []
    for c in str_arg:
        result.append(c)
        if len(result) == 58:
            break
    return result
