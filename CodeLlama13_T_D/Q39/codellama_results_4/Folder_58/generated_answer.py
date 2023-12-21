
def return_n_greatest_chars(string):
    char_count = len(set(string))
    if char_count <= 49:
        sorted_chars = sorted(string, reverse=True)
        return sorted_chars[:char_count]
    else:
        sorted_chars = sorted(string, reverse=True)
        return sorted_chars[:49]
