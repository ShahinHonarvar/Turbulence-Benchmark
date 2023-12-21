
def return_nth_smallest_ascii(string):
    char_set = set()
    for i in range(len(string)):
        if string[i].isalpha():
            char_set.add(string[i])
    sorted_chars = sorted(char_set)
    return sorted_chars[18]
