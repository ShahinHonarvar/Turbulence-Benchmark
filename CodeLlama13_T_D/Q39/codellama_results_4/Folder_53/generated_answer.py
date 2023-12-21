
def return_n_greatest_chars(string):
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    sorted_chars = sorted(char_count, key=lambda x: (char_count[x], x))
    return sorted_chars[:19]
