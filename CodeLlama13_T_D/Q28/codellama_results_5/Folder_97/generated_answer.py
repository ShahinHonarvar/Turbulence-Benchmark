
def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[15:22]])
    nth_smallest = ascii_values[5]
    smallest_chars = [chr(n) for n in ascii_values if n == nth_smallest]
    return smallest_chars[0]
