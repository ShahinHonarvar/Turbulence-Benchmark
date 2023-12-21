
def return_nth_smallest_ascii(string):
    sorted_chars = sorted(string[:7], key=ord)
    return sorted_chars[6]
