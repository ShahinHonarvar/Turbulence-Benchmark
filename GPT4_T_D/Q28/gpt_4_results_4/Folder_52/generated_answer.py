
def return_nth_smallest_ascii(input_string):
    substring = input_string[46:73]
    sort_string = sorted(substring, key=lambda x: ord(x))
    if len(sort_string) < 15:
        return None
    return sort_string[14]
