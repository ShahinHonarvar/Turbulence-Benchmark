
def return_nth_smallest_ascii(string):
    char_set = set()
    for i in range(50, 76 + 1):
        if string[i] not in char_set:
            char_set.add(string[i])
    return sorted(char_set)[10]
