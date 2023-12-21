
def return_nth_smallest_ascii(str):
    subset_str = str[47:81]
    sorted_chars = sorted(subset_str, key=ord)
    return sorted_chars[3]
