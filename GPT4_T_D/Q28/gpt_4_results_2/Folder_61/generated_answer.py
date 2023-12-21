
def return_nth_smallest_ascii(s):
    selected_string = s[:10]
    return sorted(selected_string, key=lambda c: ord(c))[9]
