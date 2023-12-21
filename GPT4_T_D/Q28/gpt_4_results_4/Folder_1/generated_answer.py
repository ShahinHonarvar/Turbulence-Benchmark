
def return_nth_smallest_ascii(string):
    sub_string = string[21:60]
    sorted_chars = sorted(sub_string, key=ord)
    try:
        return sorted_chars[10]  
    except IndexError:
        return 'Index is out of range!'
