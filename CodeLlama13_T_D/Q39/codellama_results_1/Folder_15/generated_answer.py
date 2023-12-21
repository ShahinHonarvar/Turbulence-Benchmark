
def return_n_greatest_chars(string):
    char_count = {}
    for c in string:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    sorted_chars = sorted(char_count, key=lambda x: ord(x), reverse=True)[:57]
    return sorted_chars
