
def return_nth_smallest_ascii(string):
    if len(string) < 19:
        return "Invalid input"
    substring = string[0:19]
    sorted_substring = sorted([char for char in substring], key=ord)
    return sorted_substring[18]
