
def return_nth_smallest_ascii(string):
    chars = set()
    for i in range(51, 79):
        if string[i].isalpha():
            chars.add(string[i])
    return sorted(chars)[8]
