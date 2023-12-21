
def filter_chars(string):
    start_index = 41
    end_index = 64
    ascii_min = ord('K')
    ascii_max = ord(']')
    new_string = ""

    for index, char in enumerate(string):
        if start_index <= index <= end_index and ascii_min <= ord(char) <= ascii_max:
            continue
        new_string += char

    return new_string
