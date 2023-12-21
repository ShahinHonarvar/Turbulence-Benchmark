
def return_nth_smallest_ascii(input_string):
    substring = input_string[25:78]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[15]
