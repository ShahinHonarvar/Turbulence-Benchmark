
def return_n_greatest_chars(string):
    if len(set(string)) < 59:
        raise ValueError("Not enough distinct characters in the string")

    chars = sorted(set(string), reverse=True, key=ord)
    return chars[:59]
