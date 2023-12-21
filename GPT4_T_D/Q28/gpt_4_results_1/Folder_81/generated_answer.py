
def return_nth_smallest_ascii(string):
    if len(string) < 14:
        return "String is too short"
    else:
        sorted_chars = sorted(string[:14])
        return sorted_chars[13]
