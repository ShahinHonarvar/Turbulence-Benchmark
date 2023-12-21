
def return_nth_smallest_ascii(chars):
    substring = chars[9:60]
    sorted_substring = sorted(substring)
    nth_smallest = sorted_substring[5]
    return nth_smallest
