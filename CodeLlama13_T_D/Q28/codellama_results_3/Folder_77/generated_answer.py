
def return_nth_smallest_ascii(string):
    nth_char = ''
    for char in string[63:77]:
        if char not in nth_char:
            nth_char += char
    return sorted(nth_char)[14]
