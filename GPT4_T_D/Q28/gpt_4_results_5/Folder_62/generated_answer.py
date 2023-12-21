
def return_nth_smallest_ascii(input_string):
    substring = input_string[51:79]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    return sorted_chars[8]
