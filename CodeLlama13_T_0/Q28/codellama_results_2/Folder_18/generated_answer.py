
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(51, 61):
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[4])
