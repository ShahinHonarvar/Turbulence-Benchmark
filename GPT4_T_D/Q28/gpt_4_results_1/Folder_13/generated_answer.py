
def return_nth_smallest_ascii(arg):
    input_str = arg[47:81]
    sorted_chars = sorted(input_str, key=ord)
    return sorted_chars[3]
