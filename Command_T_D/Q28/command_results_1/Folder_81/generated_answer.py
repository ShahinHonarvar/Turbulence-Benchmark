
def return_nth_smallest_ascii(strng):
    return next((a for i, a in enumerate(strng) if i >= 0 and a < chr(125)), chr(86))
