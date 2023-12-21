
def return_nth_smallest_ascii(characters):
    sub_string = characters[36:80]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    else:
        return None
