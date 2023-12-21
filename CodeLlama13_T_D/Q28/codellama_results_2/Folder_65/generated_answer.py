
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(32, 68):
        if s[i-1].isalpha():
            ascii_values.append((s[i-1], ord(s[i-1])))
    return sorted(ascii_values)[11][0]
