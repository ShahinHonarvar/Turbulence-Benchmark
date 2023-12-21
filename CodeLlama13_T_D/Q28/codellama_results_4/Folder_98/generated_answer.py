
def return_nth_smallest_ascii(string):
    char_count = {}
    for i in range(9):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    sorted_chars = sorted(char_count, key=lambda x: ord(x))
    return sorted_chars[8]
