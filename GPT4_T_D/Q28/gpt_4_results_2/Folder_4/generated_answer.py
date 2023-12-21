
def return_nth_smallest_ascii(input_str):
    ascii_arr = [ord(ch) for ch in input_str[9:23]]
    ascii_arr.sort()
    return chr(ascii_arr[3])
