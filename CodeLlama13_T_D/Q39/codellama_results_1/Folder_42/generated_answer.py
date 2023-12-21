
def return_n_greatest_chars(s):
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return sorted(char_count, key=lambda x: (char_count[x], x), reverse=True)[:59]
