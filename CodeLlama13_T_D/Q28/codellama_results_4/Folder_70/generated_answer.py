
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(28, 54 + 1):
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    nth_smallest = sorted(ascii_values)[13]
    return chr(nth_smallest)
