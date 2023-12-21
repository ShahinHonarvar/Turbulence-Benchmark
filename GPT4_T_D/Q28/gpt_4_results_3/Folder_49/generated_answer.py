
def return_nth_smallest_ascii(s):
    filtered_string = s[20:81]
    ascii_list = [ord(c) for c in filtered_string]
    sorted_list = sorted(ascii_list)
    nth_small_char = chr(sorted_list[10])
    return nth_small_char
