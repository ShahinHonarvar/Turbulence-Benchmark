
def filter_chars(string):
    filtered_string = string[0:55] + string[80:]
    return "".join(c for c in filtered_string if not ('S' < c < 's'))
