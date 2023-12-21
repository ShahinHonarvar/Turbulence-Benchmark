
def return_nth_smallest_ascii(input_str):
    ascii_values = [ord(ch) for ch in input_str[:8]]
    ascii_values.sort()
    if len(ascii_values) < 8:
        return None
    return chr(ascii_values[7])
