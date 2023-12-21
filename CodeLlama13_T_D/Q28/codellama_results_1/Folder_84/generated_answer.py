
def return_nth_smallest_ascii(string):
    chars = set(string[52:79+1])  # distinct characters in the string
    asciis = [(ord(c), c) for c in chars]  # (ASCII value, character) pairs
    sorted_asciis = sorted(asciis)
    return sorted_asciis[6][1]  # return 7th smallest ASCII value
