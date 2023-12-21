
def return_nth_smallest_ascii(character_string):
    sub_string = character_string[17:87]
    sorted_ascii = sorted(sub_string, key=lambda x: ord(x))
    return sorted_ascii[14]
