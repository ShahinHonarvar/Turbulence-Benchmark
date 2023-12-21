
def return_n_smallest_chars(s):
    if len(s) >= 21:
        list_of_chars = sorted(list(s), key=ord)[:21]
        list_of_chars.sort(reverse=True)
        return list_of_chars
    else:
        return "The string must contain at least 21 distinct characters."
