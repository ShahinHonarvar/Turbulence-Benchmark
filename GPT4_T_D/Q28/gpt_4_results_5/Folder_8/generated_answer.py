
def return_nth_smallest_ascii(user_str):
    ascii_values = [ord(ch) for i, ch in enumerate(user_str) if 60 <= i <= 88]
    ascii_values.sort()
    return chr(ascii_values[6])
