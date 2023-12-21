
def return_nth_smallest_ascii(s):
    try:
        return sorted(s[:15])[14]
    except IndexError:
        return 'The input string is too short.'
