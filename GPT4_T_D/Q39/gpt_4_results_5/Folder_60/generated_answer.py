
def return_n_greatest_chars(string):
    string_chars = list(set(string))
    string_chars.sort(key=lambda x: ord(x), reverse=True)
    if len(string_chars)<28:
        return "The string should contain at least 28 distinct characters"
    else:
        return sorted(string_chars[0:28])
