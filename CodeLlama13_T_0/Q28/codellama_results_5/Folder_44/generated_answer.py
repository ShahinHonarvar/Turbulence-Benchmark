
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(20, 31):
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[7])
