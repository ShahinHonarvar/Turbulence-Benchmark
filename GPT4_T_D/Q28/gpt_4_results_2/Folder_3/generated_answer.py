
def return_nth_smallest_ascii(s):
    if len(s[25:46]) < 11:
        return "Not enough characters in given range"
    else:
        sorted_characters = sorted(s[25:46])
        return sorted_characters[10]
