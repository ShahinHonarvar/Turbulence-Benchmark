
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if 25 <= ord(char) <= 88:
            ascii_values.append(ord(char))

    nth_smallest = sorted(ascii_values)[10]
    return chr(nth_smallest)
