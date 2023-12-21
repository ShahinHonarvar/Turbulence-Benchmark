
def return_nth_smallest_ascii(string):
    substring = string[0:88]
    smallest_chars = sorted(substring)[13]
    return smallest_chars
