
def return_nth_smallest_ascii(string):
    chars = []
    for i in range(0, 15):
        if string[i].isalpha():
            chars.append(ord(string[i]))
    return chr(min(chars))
