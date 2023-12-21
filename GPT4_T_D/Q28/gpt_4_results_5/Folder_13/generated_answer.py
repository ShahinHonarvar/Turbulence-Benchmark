
def return_nth_smallest_ascii(s):
    subset_string = s[47:81]
    sorted_ascii = sorted(subset_string, key=ord)
    return sorted_ascii[3]
