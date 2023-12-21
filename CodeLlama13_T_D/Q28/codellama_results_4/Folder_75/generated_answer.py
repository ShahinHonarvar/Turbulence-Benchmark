
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(62, 84):
        if s[i-1].isalpha():
            ascii_values.append(ord(s[i-1]))
    return chr(sorted(ascii_values)[8])
