
def return_nth_smallest_ascii(string):
    # find the characters between indices 38 and 64, both inclusive
    chars = []
    for i in range(38, 65):
        if string[i].isalpha():
            chars.append(string[i])

    # sort the characters by their ASCII value
    sorted_chars = sorted(chars, key=lambda x: ord(x))

    # return the character with the 14th smallest ASCII value
    return sorted_chars[13]
